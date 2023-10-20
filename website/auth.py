
from flask import Blueprint, render_template, flash, redirect, url_for, request, jsonify
from .models import Admin
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from sqlalchemy import func
from . import db


@auth.route('/admin/login', methods=['GET', 'POST'])
def seller_login():
    if request.method == 'POST':
        user_name = request.form.get('user_name')
        password = request.form.get('password')
        user =Admin.query.filter_by(user_name=user_name, is_seller=True).first()
        if user and check_password_hash(user.password, password):
            flash('Logged in', category='success')
            login_user(user, remember=True)
            return redirect(url_for('web_views.sell', app_name=app_name))
        else:
            flash("Incorrect username or password", category='error')
    return render_template('/seller_functions/seller_login.html', app_name=app_name)
