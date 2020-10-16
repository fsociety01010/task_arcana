from app import db
from datetime import date


class Client(db.Model):
    __bind_key__ = 'dbClient'
    id = db.Column(db.INTEGER, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50), nullable=False)
    phone_number = db.Column(db.INTEGER, nullable=False, unique=True)
    birthday = db.Column(db.DateTime)
    email = db.Column(db.String)


class House(db.Model):
    __bind_key__ = 'dbHouse'
    id = db.Column(db.INTEGER, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(50), nullable=False)
    type = db.Column(db.String(50), nullable=False)
    rooms = db.Column(db.INTEGER, nullable=False)
    price = db.Column(db.INTEGER, nullable=False)
    description = db.Column(db.String(500))
    owner = db.Column(db.String)
    owner_id = db.Column(db.INTEGER)
    dateCreation = db.Column(db.String, default=date.today().strftime("%d/%m/%Y"))

