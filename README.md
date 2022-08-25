# SQLAlchemy Profiling

This is a python project that collects statistics about SQL queries
rendered with SQLAlchemy ORM with a SQLite database and save them in a json file "results.json".

Collected data are :

- Database Type
- Database Name
- Connection Open Time
- SQL Query
- SQL Table
- SQL Query Type (SELECT, DELETE, UPDATE, INSERT etc...)
- Query Time
- Row Count

This project can help in profiling SQL queries and optimizing them. It can be used with any SQL database.

## About SQLAlchemy

SQLAlchemy is an open-source SQL toolkit and object-relational mapper for the Python programming language.

# Setup Virtual Environment

It is highly **recommended** to use a Python virtual enrionment.

## Create virtual environment

This commande should be launched only once

```python
python -m venv venv
```

## Activate virtual environment

This command should be launch every time you start your PC

```bash
venv\scripts\activate
```

# Start the application

```
$env:FLASK_APP = "runner.py"
pip install -r requirements.txt
flask run
```

## Desactivate virtual environment

```
deactivate
```

---
