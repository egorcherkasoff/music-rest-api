from database import db
from datetime import datetime


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    created = db.Column(db.DateTime, default=datetime.now())
    updated = db.Column(db.DateTime, nullable=True, default=None)
    deleted = db.Column(db.DateTime, nullable=True, default=None)
