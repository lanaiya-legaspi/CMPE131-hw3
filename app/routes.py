from app import myapp_obj
from flask import render_template, redirect, request
from app.forms import LoginForm, RecipeForm
from app.models import User, Recipe
from app import db
from datetime import datetime

@myapp_obj.route("/", methods=["GET","POST"])
@myapp_obj.route("/recipes", methods=["GET","POST"])
def main():
	username = "user04732"
	recipes = Recipe.query.all()
	return render_template("recipes.html", username=username, recipes=recipes)


@myapp_obj.route("/add-recipe", methods=["GET", "POST"])
def new_recipe():
	form = RecipeForm()

	if request.method == "POST":
		title = request.form['title']
		desc = request.form['description']
		ings = request.form['ingredients']
		insns = request.form['instructions']
		tmstmp = str(datetime.now().strftime("%m-%d-%Y"))
		recipe = Recipe(title=title, description=desc, ingredients=ings, instructions=insns, created=tmstmp)
		db.session.add(recipe)
		db.session.commit()
		print("New recipe added!")
		return redirect(url_for("recipes"))
	else:
		print("MOOO MOOO")
	return render_template("add-recipe.html", form=form)


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

@myapp_obj.route("/register")
def register():
	form = LoginForm()
	if form.validate_on_submit():
		return redirect("/")
	else:
		print("MOOO MOOO")
	return render_template("register.html", form=form)
