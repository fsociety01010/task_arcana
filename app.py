from flask import Flask, Blueprint, render_template, url_for, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///arcanaApp.db'
app.config['SECRET_KEY'] = 'IDONTKNOWEHATTOPUTHERE123%$!@&;'
db = SQLAlchemy(app)

app.register_blueprint(Blueprint('app', __name__))

login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

import auth
import models

# Show all list of announcements
@app.route('/', methods=['GET'])
def index():
    print(current_user)
    all_house = models.getAllHouse()
    return render_template('index.html', houses=all_house)


# Show the details of certain announcement
@app.route('/house/<int:id>', methods=['GET'])
def houseById(id):
    house = models.getHouseById(id)
    return render_template('houseDetail.html', house=house)


# Can update the information about the house if you are the owner
@app.route('/house/edit/<int:id>', methods=['GET', 'POST'])
def editAnnouncementById(id):
    if request.method == 'GET':
        house = models.getHouseById(id)
        if house.author_id == current_user.id:
            return render_template('editHouse.html', house=house)
        else:
            return "Not permitted"
    elif request.method == 'POST':
        house = models.getHouseById(id)
        if house.author_id == current_user.id:
            models.editHouse(request)
            return redirect(url_for('index'))
        else:
            return "Not permitted"


# It's possible to delete the house if you are the owner
@app.route('/house/delete/<int:id>', methods=['GET'])
def deleteHouseById(id):
    house = models.getHouseById(id)
    if house.author_id == current_user.id:
        models.deleteHouse(house.id)
        return redirect(url_for('index'))
    else:
        return "Not permitted"


# Add the new announcement to the DB
@app.route('/add/announcement', methods=['GET', 'POST'])
def addAnnouncement():
    if request.method == 'GET':
        return render_template('addAnouncement.html')
    else:
        models.addHouse(request)
        return redirect(url_for('index'))



# Show the information about the user and his announcement
@app.route('/user/<int:id>', methods=['GET'])
def infoUser(id):
    user = models.getUserByid(id)
    houses = models.getHouseByUser(id)
    return render_template('userDetails.html', houses=houses, user=user)


# Update/Edit information about current user
@app.route('/user/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def editUser(id):
    if (request.method == "GET"):
        user = models.getUserByid(id)

        if (current_user.id == user.id):
            return render_template('editUser.html')
        else:
            return "Not permitted"
    else:
        user = models.getUserByid(id)
        if (current_user.id == user.id):
            models.updateUserInformation(request)
            return redirect(url_for("index"))
        else:
            return "Not permitted"


# Show the list of the cities of announcement
@app.route('/search/cities', methods=['GET', 'POST'])
def allCities():
    allCities = models.getAllLocations()
    return render_template('allCities.html', allCities=allCities)


# Show the announcement in certain city
@app.route('/search/city/<string:city>', methods=['GET'])
def allAHouseByCity(city):
    all_house = models.getHouseByCity(city)
    return render_template('houseByCity.html', houses=all_house, city=city)


# Error page
@app.errorhandler(404)
def page_not_found(error):
    # return render_template('page_not_found.html'), 404
    return "NOT FOUND"


if __name__ == '__main__':
    app.run(debug=True)
