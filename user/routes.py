from app import db
from user import user_blueprint
from user.model import User
from flask import jsonify, request


@user_blueprint.route("/", methods=["GET"])
def get_users():
    users = User.query.all()
    return jsonify(users)


@user_blueprint.route("/", methods=["POST"])
def add_user():
    user = User(username="Test", email="Test@test.com")
    db.session.add(user)
    db.session.commit()
    return jsonify("success"), 200


@user_blueprint.route("/", methods=["DELETE"])
def delete_user():
    User.query.filter_by(username="Test").delete()
    db.session.commit()
    return jsonify("success"), 200


@user_blueprint.route("/", methods=["PUT"])
def update_user():
    user = User.query.filter_by(id=1)
    user.update({"username": "Test3 "}, synchronize_session=False)
    return jsonify("success"), 200
