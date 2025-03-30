from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmimtField, validators

class LoginForm(FlaskForm):
	username = StringField('USERNAME', validators=[validators.DataRequired()])
	password = PasswordField('PASSWORD', validators=[validators.Length(min=4, max=35)])
	submit = SubmitField("Sign In")
	remember_me = BooleanField("Remember Me")
