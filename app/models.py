from app import db

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(32))
	password = db.Column(db.String(32))
	email = db.Column(db.String(32))
	remember_me = db.Column(db.Boolean)

class Recipe(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(80))
	description = db.Column(db.Text)
	ingredients = db.Column(db.Text)
	instructions = db.Column(db.Text)
	created = db.Column(db.DateTime)
