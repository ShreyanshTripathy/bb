from flask import Flask, render_template, request, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired
from flask_ckeditor import CKEditorField

app = Flask(__name__)
app.config['SECRET_KEY'] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
Bootstrap(app)

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///Parcel.db"
db = SQLAlchemy(app)

# Define a SQLAlchemy model for the data
class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    body = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(200), nullable=False)

# Define a form to add events
class EventForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    body = CKEditorField('Body', validators=[DataRequired()])
    image_url = StringField('Image URL', validators=[DataRequired()])

# Define a form for the word input
class WordForm(FlaskForm):
    word = StringField('Enter the Word', validators=[DataRequired()])

@app.route('/add', methods=['GET', 'POST'])
def add():
    form = EventForm()
    if form.validate_on_submit():
        title = form.title.data
        body = form.body.data
        image_url = form.image_url.data
        event = Event(title=title, body=body, image_url=image_url)
        db.session.add(event)
        db.session.commit()
        flash('Event added successfully', 'success')
        return redirect(url_for('home'))
    return render_template("add.html", form=form)

@app.route('/', methods=['GET', 'POST'])
def home():
    form = WordForm()
    if form.validate_on_submit():
        word = form.word.data.lower()  # Convert to lowercase for case-insensitive check
        if word == 'basketball':
            return redirect(url_for('add'))
        else:
            flash('Invalid word. Please enter "Basketball".', 'error')
    events = Event.query.all()
    return render_template("home.html", form=form, events=events)

if __name__ == "__main__":
    app.run(debug=False, port=5000)
