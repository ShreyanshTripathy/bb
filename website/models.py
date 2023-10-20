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


class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    member_name = db.Column(db.String(100), nullable=False)
    team_name = db.Column(db.String(100), nullable=False)
    captain = db.Column(db.Boolean, default=False)

    matches = db.relationship('Match')

class Match(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    team_a_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)
    team_b_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)
    date_time = db.Column(db.DateTime, default=func.now())
    team_a_score = db.Column(db.Integer)
    team_a_score = db.Column(db.Integer)

    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'), nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), nullable=False)

