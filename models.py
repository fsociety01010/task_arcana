from datetime import datetime

import sqlalchemy

from app import db


class Client(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.INTEGER, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50), nullable=False)
    phone_number = db.Column(db.String(5), nullable=False, unique=False)
    birthday = db.Column(db.String(11),nullable=False)
    email = db.Column(db.String, nullable=False, unique=False)
    password = db.Column(db.INTEGER, nullable=False)

    def __repr__(self):
        return 'Client created with id:' + str(self.id)

#rebuild
# TO DO
def addUser():
    new_client = Client(
        name='Alex',
        surname='Agarkov',
        phone_number='10621a079526',
        birthday=datetime.utcnow(),
        email='alea1xbmaaaax@mail.ua',
        password=123
    )
    db.session.add(new_client)
    db.session.commit()

def updateUserInformation(request):
    id_ = request.form['id']
    client = Client.query.filter(Client.id == id_).first()
    client.name = request.form['name']
    client.surname = request.form['surname']
    client.phone_number = request.form['phone_number']
    client.birthday = request.form['birthday']
    client.email = request.form['email']
    client.password = request.form['password']

    userAnnouncement = House.query.filter(House.author_id == client.id).all()
    for announcement in userAnnouncement:
        announcement.author = client.name + " " + client.surname

    db.session.commit()

def getUserByid(id):
    return Client.query.get(id)


class House(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.INTEGER, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(50), nullable=False)
    type = db.Column(db.String(50), nullable=False)
    rooms = db.Column(db.INTEGER, nullable=False)
    price = db.Column(db.INTEGER, nullable=False)
    description = db.Column(db.Text, nullable=False)
    author = db.Column(db.String, nullable=False)
    author_id = db.Column(db.INTEGER, nullable=False)
    dateCreation = db.Column(db.DateTime, nullable=False, default=sqlalchemy.sql.func.now() )

    def __repr__(self):
        return 'Announcement created with id:' + str(self.id)


# python
# from models import db  - WARNING import db only from the .py where u have models
# db.create_all()
# from models import House


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


def getHouseById(id):
    return House.query.get(id)


def getHouseByUser(userId):
    return House.query.filter(House.author_id == userId).all()


def deleteHouse(id):
    House.query.filter(House.id == id).delete()
    db.session.commit()

def editHouse(request):
    id_ = request.form['id']
    house = House.query.filter(House.id == id_).first()
    house.title = request.form['title']
    house.location = request.form['location']
    house.type = request.form['type']
    house.rooms = request.form['rooms']
    house.price = request.form['price']
    house.description = request.form['description']
    db.session.commit()

def getAllLocations():
    assurances = []
    for assurance in House.query.distinct(House.location):
        if assurance.location not in assurances:
            assurances.append(assurance.location)
    return list(set(assurances))


def getHouseByCity(city):
    return House.query.filter(House.location == city).all()
