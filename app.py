import json
import time
from pprint import pprint
from flask import Flask, logging
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import event
from sqlalchemy.engine import Engine
import logging

# SQLAlchemy Instance
db = SQLAlchemy()

# Dictionnary to save query data
query_data = {}

# List to save each queries data
queries_data_list = []

# Logging, maybe it would help too
logging.basicConfig()
logger = logging.getLogger("myapp.sqltime")
logger.setLevel(logging.DEBUG)


# Function to filter query type and table name
def filter_query(query: str):
    x = query.split(" ")
    if x[0] == "SELECT":
        index = x.index("\nFROM")
        return {
            "query_table": x[index + 1],
            "query_type": x[0],
        }
    if x[0].strip() in ["INSERT", "DELETE", "CREATE", "DROP"]:
        return {
            "query_table": x[2],
            "query_type": x[0].strip(),
        }
    if x[0].strip() == "UPDATE":
        return {
            "query_table": x[1],
            "query_type": x[0].strip(),
        }
    if x[0] == "PRAGMA":
        return {
            "query_table": x[1].split('"')[1],
            "query_type": x[0],
        }


@event.listens_for(Engine, "before_cursor_execute")
def before_cursor_execute(conn, cursor, statement, parameters, context, executemany):
    # Logging
    conn.info.setdefault("query_start_time", []).append(time.time())
    logger.debug("Start Query: %s", statement)
    # Data retrieved before cursour execution
    query_data["db_type"] = conn.engine.name
    query_data["db_name"] = conn.engine.url.database
    query_data[
        "connection_opened_at"
    ] = conn._dbapi_connection._connection_record.starttime
    query_data["query_sql"] = statement
    query_data["query_table"] = filter_query(statement)["query_table"]
    query_data["query_type"] = filter_query(statement)["query_type"]


@event.listens_for(Engine, "after_cursor_execute")
def after_cursor_execute(conn, cursor, statement, parameters, context, executemany):
    global query_data
    # Calculate total time
    total = time.time() - conn.info["query_start_time"].pop(-1)
    logger.debug("Query Complete!")
    logger.debug("Total Time: %f", total)
    query_data["query_time"] = total
    query_data["row_count"] = cursor.rowcount
    # add the query data to the list
    queries_data_list.append(query_data)
    # Reset query_data
    query_data = {}
    # Save the list into a json file
    data = json.dumps(queries_data_list)
    with open("query_data_list.json", "w") as outfile:
        outfile.write(data)


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)
    from user import user_blueprint

    app.register_blueprint(user_blueprint)
    return app
