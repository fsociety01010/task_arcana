from flask import url_for, redirect, flash
from app import check_password_hash, app, request, render_template, login_manager, login_user, current_user, login_required, logout_user
import models

@login_manager.user_loader
def load_user(user_id):
    return models.Client.query.get(user_id)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        email = request.form.get('email')
        password = request.form.get('password')
        remember = True

        user = models.Client.query.filter_by(email=email).first()

        if not user and not check_password_hash(user.password, password):
            # flash('Please check your login details and try again.')
            return redirect(url_for('login'))

        login_user(user, remember=remember)

        return redirect(url_for('index'))


# Add the new user to the DB, sign up
@app.route('/signUp', methods=['GET', 'POST'])
def signUp():
    if request.method == 'GET':
        if current_user.is_authenticated:
            return redirect(url_for('index'))
        else:
            return render_template('signUp.html')
    else:
        email = request.form.get('email')
        user = models.Client.query.filter_by(email=email).first()

        if user:
            flash('Email address already exists.')
            return redirect(url_for('signUp'))

        models.addClient(request)
        return redirect(url_for('index'))


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))
