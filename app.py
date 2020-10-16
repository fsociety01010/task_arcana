from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/house', methods=['GET', 'POST'])
def house():
    return render_template("house.html")


if __name__ == '__main__':
    app.run(debug=True)

