from app import myapp_obj
from flask import render_template, redirect
from app.forms import LoginForm, RecipeForm
from app.models import User #, RecipeList
from app import db

@myapp_obj.route("/")
@myapp_obj.route("/recipes")
def main():
	username = "user04732"
#	recipes = RecipeList()
	return render_template("recipes.html", username=username)


@myapp_obj.route("/recipes/new")
def new_recipe():
	form = RecipeForm()
	if form.validate_on_submit():
		return redirect("/")
	else:
		print("MOOO MOOO")
	return render_template("new-recipes.html", form=form)


@myapp_obj.route("/accounts")
def users():
	return "My USER ACCOUNTS"

@myapp_obj.route("/login", methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		print(f"Here is the input from the user: {form.username.data} and {form.password.data}")
		return redirect("/")
	else:
		print("MOOOO MOOO")
	return render_template("login.html", form=form)
