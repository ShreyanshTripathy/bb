from . import db
from flask_login import UserMixin
from sqlalchemy import func, ForeignKey


class Admin(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(30))


    #relationships
    events = db.relationship('Event')
    matches = db.relationship('Match')

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    img_url = db.Column(db.String(255), nullable=False)
    start_date = db.Column(db.DateTime, default=func.now())
    end_date = db.Column(db.DateTime, default=func.now())

    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'), nullable=False)

    # relationships
    matches = db.relationship('Match')


class Match(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    team_a = db.Column(db.String(100), nullable=False)
    team_b = db.Column(db.String(100), nullable=False)
    date_time = db.Column(db.DateTime, default=func.now())

    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'), nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), nullable=False)

