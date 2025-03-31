from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, validators

class LoginForm(FlaskForm):
	username = StringField('USERNAME', validators=[validators.DataRequired()])
	password = PasswordField('PASSWORD', validators=[validators.Length(min=4, max=35)])
	submit = SubmitField("Sign In")
	remember_me = BooleanField("Remember Me")


class RecipeForm(FlaskForm):
	title = StringField('RECIPE', validators=[validators.DataRequired()])
	description = TextAreaField('Description', validators=[validators.DataRequired()])
	ingredients = TextAreaField('Ingredients', validators=[validators.DataRequired()])
	instructions = TextAreaField('Instructions', validators=[validators.DataRequired()])
	submit = SubmitField("Submit Recipe")
