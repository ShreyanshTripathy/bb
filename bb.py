from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.validators import DataRequired
from flask_ckeditor import CKEditorField
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
Bootstrap5(app)

# Creating Database
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///Event.db"
db = SQLAlchemy()
db.init_app(app)

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    body = db.Column(db.Text, nullable=False)
    image_filename = db.Column(db.String(255), nullable=False)
    buttun_url = db.Column(db.String(200), nullable=False)

class EventForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    body = CKEditorField('Body', validators=[DataRequired()])
    image = FileField('Upload Image', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')])
    buttun_url = StringField('Button URL', validators=[DataRequired()])
    submit = SubmitField("Submit")

class WordForm(FlaskForm):
    word = PasswordField('Enter the Word', validators=[DataRequired()])

with app.app_context():
    db.create_all()

@app.route('/add', methods=['GET', 'POST'])
def add():
    form = EventForm()
    if form.validate_on_submit():
        image = form.image.data
        if image:
            image_filename = secure_filename(image.filename)  # Get a secure filename
            image.save(os.path.join("static", "assets", "img", image_filename))  # Save the image to the correct folder

        new_event = Event(
            title=form.title.data,
            body=form.body.data,
            image_filename=image_filename,
            buttun_url=form.buttun_url.data
        )
        db.session.add(new_event)
        db.session.commit()
        return redirect(url_for('home'))

    return render_template("add.html", form=form)

@app.route('/login', methods=['GET', 'POST'])
def add_Event():
    form = WordForm()
    if form.validate_on_submit():
        if form.word.data == "Basketball":
            return redirect(url_for('add'))
        else:
            return redirect(url_for('home'))
    return render_template("login.html", form=form)

@app.route('/')
def home():
    events = Event.query.all()  # Fetch a list of Event objects from the database
    return render_template("home.html", events=events)

@app.route('/contact')
def contact():
    return render_template("contact.html")
if __name__ == "__main__":
    app.run(debug=True, port=5000)
