from flask import Blueprint

user_blueprint = Blueprint("user_blueprint", __name__, url_prefix="/users")

from . import routes