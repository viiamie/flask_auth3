from flask_wtf import FlaskForm
from wtforms import validators
from wtforms.fields import *

class csv_upload(FlaskForm):
    file = FileField()
    submit = SubmitField()

class edit_location_form(FlaskForm):
    title = TextAreaField('Location Name', [validators.DataRequired(), validators.length(max=300)], description="Enter the name of the location")
    longitude = TextAreaField('Longitude', [validators.DataRequired(), validators.length(max=300)], description="Enter the longitude")
    latitude = TextAreaField('Latitude', [validators.DataRequired(), validators.length(max=300)], description="Enter the latitude")
    population = IntegerField('Population', [validators.DataRequired()], description="Enter the population")
    submit = SubmitField()

class add_location_form(FlaskForm):
    title = TextAreaField('Location Name', [
        validators.DataRequired(),
        validators.length(max=300)
    ], description="Name of the location")

    longitude = TextAreaField('Longitude', [
        validators.DataRequired(),
        validators.length(max=300)
    ], description="Longitude of the location")

    latitude = TextAreaField('Latitude', [
        validators.DataRequired(),
        validators.length(max=300)
    ], description="Latitude of the location")

    population = IntegerField('Population', [
        validators.DataRequired(),
    ], description="Population of the location")

    submit = SubmitField()