import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'cookbookDb'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_top_recipes')
def get_top_recipes():
    return render_template("home.html", recipes=mongo.db.recipes.find())

@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('get_top_recipes'))
    
@app.route('/add_recipe')
def add_recipe():
    return render_template("add_recipe.html")
    
@app.route('/get_recipe_names')
def get_recipe_names():
    return render_template("index.html", names=mongo.db.recipe_names.find())
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)