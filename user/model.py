from dataclasses import dataclass

from app import db


@dataclass
class User(db.Model):
    id: int
    username: str
    email: str

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)
