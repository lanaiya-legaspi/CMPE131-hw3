from app import myapp_obj
from flask import render_template, redirect, request
from app.forms import LoginForm, RecipeForm
from app.models import User, Recipe
from app import db
from datetime import datetime

# View Recipes page
@myapp_obj.route("/", methods=["GET","POST"])
@myapp_obj.route("/recipes", methods=["GET","POST"])
def main():
	username = "user04732"
	recipes = Recipe.query.all()
	return render_template("recipes.html", username=username, recipes=recipes)

#Create New Recipes page
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

#Edit Recipe page
@myapp_obj.route("/edit-recipe/<id>", methods=["GET", "POST"])
def edit_recipe(id):
	form = RecipeForm()
	recipe = Recipe.query.filter(Recipe.id==id).first()
	form.title.data = recipe.title
	form.description.data = recipe.description
	form.ingredients.data = recipe.ingredients
	form.instructions.data = recipe.instructions

	if request.method == "POST":
		recipe.title = request.form['title']
		recipe.description = request.form['description']
		recipe.ingredients = request.form['ingredients']
		recipe.instructions = request.form['instructions']
		recipe.created = str(datetime.now().strftime("%m-%d-%Y"))
		db.session.commit()
		print("Recipe edited!")
		return redirect(url_for("recipes"))
	return render_template("edit-recipe.html", form=form)

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
