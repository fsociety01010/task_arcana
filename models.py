from datetime import datetime
from app import db


class Client(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50), nullable=False)
    phone_number = db.Column(db.INTEGER, nullable=False, unique=True)
    birthday = db.Column(db.DateTime)
    email = db.Column(db.String)

    def __repr__(self):
        return 'Client created with id:' + str(self.id)


def addClient():
    new_client = Client(
        name='Alex',
        surname='Agarkov',
        phone_number=621079526,
        birthday=datetime.utcnow(),
        email='alexbmx@mail.ua'
    )
    db.session.add(new_client)
    db.session.commit()

def getUserByid(id):
    return Client.query.get(id)



class House(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(50), nullable=False)
    type = db.Column(db.String(50), nullable=False)
    rooms = db.Column(db.INTEGER, nullable=False)
    price = db.Column(db.INTEGER, nullable=False)
    description = db.Column(db.Text, nullable=False)
    author = db.Column(db.String, nullable=False)
    author_id = db.Column(db.INTEGER, nullable=False)
    dateCreation = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())

    def __repr__(self):
        return 'Announcement created with id:' + str(self.id)


# python
# from models import db  - WARNING import db only from the .py where u have models
# db.create_all()
# from models import House


# Implementation all CRUD operations
def addHouse(house):
    db.session.add(house)
    db.session.commit()


def createHouse(request):
    title_ = request.form['title']
    location_ = request.form['location']
    type_ = request.form['type']
    rooms_ = request.form['rooms']
    price_ = request.form['price']
    description_ = request.form['description']
    author_ = request.form['author']
    author_id_ = request.form['author_id']
    return House(title=title_, location=location_, type=type_, rooms=rooms_, price=price_,
                 description=description_, author_id=author_id_, author=author_)


def getAllHouse():
    return House.query.order_by(House.dateCreation).all()


def update():
    house = House.query.get(id)


def getHouseById(id):
    return House.query.get(id)


getHouseById(1)


def deleteHouse(id):
    House.query.filter(House.id == id).delete()
    db.session.commit()

