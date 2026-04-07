# Add any form classes for Flask-WTF here
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField
from wtforms.validators import DataRequired, Length

class MovieForm(FlaskForm):
    title = StringField('Movie Title', validators=[
        DataRequired(message='Title is required.'),
        Length(max=100, message='Title cannot exceed 100 characters.')
    ])
    
    description = TextAreaField('Description', validators=[
        DataRequired(message='Description is required.')
    ])
    
    poster = FileField('Movie Poster', validators=[
        DataRequired(message='Please upload a poster image.')
    ])