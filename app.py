from flask import Flask, render_template, url_for, session, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///houses.db'
db = SQLAlchemy(app)
import models

all_user = [
    {
        'name': 'Alex',
        'surname': 'Agarkov',
        'birthday': "22/03/1996",
        'id': 1,
        "password": 1
    },
    {
        'name': 'Ira',
        'surname': 'Agarkov',
        'birthday': "29/06/1998",
        'id': 2,
        "password": 2
    }
]
current_user_id = all_user[0]['id']

#WORK
# Show all list of house with "GET"
# Can click at some house and it will pass to the announcement
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        all_house = models.getAllHouse()
        return render_template('index.html', list_house=all_house, user_id=current_user_id)
    else:
        house = models.createHouse(request)
        models.addHouse(house)
        all_house = models.getAllHouse()
        return render_template('index.html', list_house=all_house, user_id=current_user_id)

#WORK
# Show the details of certain announcement
@app.route('/house/<int:id>', methods=['GET'])
def houseById(id):
    house = models.getHouseById(id)
    return render_template('house_detail.html', house=house)


# Can update the information about the house if you are the owner
@app.route('/house/edit/<int:id>', methods=['GET', 'POST'])
def editHouseById(id):
    house = models.getHouseById(id)
    if house.author_id == current_user_id:
        return render_template('edit_house.html', house=house)
    else:
        return "Not permitted"

#WORK
# Can delete the house if you are the owner
@app.route('/house/delete/<int:id>', methods=['GET'])
def deleteHouseById(id):
    house = models.getHouseById(id)
    if house.author_id == current_user_id:
        models.deleteHouse(house.id)
        return redirect(url_for('index'))
    else:
        return "Not permitted"

#WORK
@app.route('/user/<int:id>', methods=['GET'])
def infoUser(id):
    user = models.getUserByid(id)
    return render_template('user_details.html', user=user)


@app.route('/user/edit/<int:id>', methods=['GET', 'POST'])
def editUser(id):
   user = models.getUserByid(id)
   return render_template('user_details.html', user = user)


@app.route('/search/city', methods=['GET', 'POST'])
def allCities():
    # Show the list of cities
    return "cities......."


@app.route('/search/city/<string:city>', methods=['GET', 'POST'])
def allHotelsInCity(city):
    # Show the list  house in the city
    # get all house from city
    return "list of the house in city " + city


@app.errorhandler(404)
def page_not_found(error):
    # return render_template('page_not_found.html'), 404
    return "NOT FOUND"


if __name__ == '__main__':
    app.run(debug=True)
