from flask import Flask
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


db = SQLAlchemy()
DB_NAME = 'basketball_db.sqlite3'


def create_app():
    app = Flask(__name__)
    app.debug = True
    app.config['SECRET_KEY'] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
    
    # Bootstrap5(app)

    # Creating Database
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db = SQLAlchemy()
    db.init_app(app)

    from .views import views
    app.register_blueprint(views)


    with app.app_context():
        db.create_all()

    return app
