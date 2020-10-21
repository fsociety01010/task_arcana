from flask import Flask, render_template, url_for, session, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///arcanaApp.db'
db = SQLAlchemy(app)

import models

current_user_id = 1


# WORK
# Show all list of house with "GET"
# Can click at some house and it will pass to the announcement
@app.route('/', methods=['GET'])
def index():
    all_house = models.getAllHouse()
    return render_template('index.html', houses=all_house, user_id=current_user_id)


# WORK
# Show the details of certain announcement
@app.route('/house/<int:id>', methods=['GET'])
def houseById(id):
    house = models.getHouseById(id)
    return render_template('house_detail.html', house=house, user_id=current_user_id)


# work
# CSS PROBLEM
# Can update the information about the house if you are the owner
@app.route('/house/edit/<int:id>', methods=['GET', 'POST'])
def editHouseById(id):
    house = models.getHouseById(id)
    if house.author_id == current_user_id:
        return render_template('editHouse.html', house=house)
    else:
        return "Not permitted"


# WORK
# Can delete the house if you are the owner
@app.route('/house/delete/<int:id>', methods=['GET'])
def deleteHouseById(id):
    house = models.getHouseById(id)
    if house.author_id == current_user_id:
        models.deleteHouse(house.id)
        return redirect(url_for('index'))
    else:
        return "Not permitted"


# WORK
@app.route('/add/announcement', methods=['GET', 'POST'])
def addAnouncement():
    if request.method == 'GET':
        return render_template('addAnouncement.html', user_id=current_user_id)
    else:
        house = models.createHouse(request)
        models.addHouse(house)
        all_house = models.getAllHouse()
        return redirect(url_for('index'))


# WORK
@app.route('/user/<int:id>', methods=['GET'])
def infoUser(id):
    user = models.getUserByid(id)
    houses = models.getHouseByUser(id)
    return render_template('user_details.html', user=user, houses = houses, user_id = current_user_id)

#work
# only css
@app.route('/user/edit/<int:id>', methods=['GET', 'POST'])
def editUser(id):
    user = models.getUserByid(id)
    if (current_user_id == user.id):
        return render_template('edit_user.html', user=user)
    else:
        return "Not permitted"


@app.route('/search/cities', methods=['GET', 'POST'])
def allCities():
    allCities = models.getAllLocations()
    return render_template('allCities.html', allCities=allCities, user_id=current_user_id)

#Work
#Only CSS
@app.route('/search/city/<string:city>', methods=['GET', 'POST'])
def allAHouseByCity(city):
    all_house = models.getHouseByCity(city)
    return render_template('houseByCity.html', houses=all_house, user_id=current_user_id, city=city)


@app.errorhandler(404)
def page_not_found(error):
    # return render_template('page_not_found.html'), 404
    return "NOT FOUND"


if __name__ == '__main__':
    app.run(debug=True)
