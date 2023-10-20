
from flask import Blueprint, render_template, flash, redirect, url_for, request
from .models import Admin
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from sqlalchemy import func
from . import db

auth = Blueprint('web_auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def seller_login():
    if request.method == 'POST':
        user_name = request.form.get('user_name')
        password = request.form.get('password')
        user =Admin.query.filter_by(user_name=user_name).first()
        if user and check_password_hash(user.password, password):
            flash('Logged in', category='success')
            login_user(user, remember=True)
            return redirect(url_for('web_views.sell'))
        else:
            flash("Incorrect username or password", category='error')
    return render_template('login.html')


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        user_name = request.form.get('user_name')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        
        if password != confirm_password:
            flash("Passwords aren't matching", category='error')
        elif len(password) < 5:
            flash("Password is too short use at least 5 letters", category='error')
        else:
            new_user = Admin(user_name=user_name, password=generate_password_hash(password, method='sha256'))

            db.session.add(new_user)
            db.session.commit()

            flash("Whoa! Your account is successfully created.", category='success')
            login_user(new_user, remember=True)
            return redirect(url_for('views.home'))

    return render_template('sign-up.html')
