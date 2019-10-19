import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'cookbookDb'
#app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')
app.config["MONGO_URI"]="mongodb+srv://root-user96:r00tUser96@myfirstcluster-ehz2d.mongodb.net/cookbookDb?retryWrites=true&w=majority"


mongo = PyMongo(app)

@app.route('/')
@app.route('/get_top_recipes')
def get_top_recipes():
    return render_template("home.html", recipes=mongo.db.recipes.find())

@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template('edit_recipe.html', recipe=the_recipe)

@app.route('/show_recipe/<recipe_id>')
def show_recipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template('show_recipe.html', recipe=the_recipe )

@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('get_top_recipes'))

@app.route('/add_like_to_recipe/<recipe_id>', methods=['GET'])
def add_like_to_recipe(recipe_id):
    recipes = mongo.db.recipes
    
    recipes.update(
        {'_id': ObjectId(recipe_id)},
        { '$inc': { 'likes': +1} }
    )
        
    return redirect(url_for('show_recipe', recipe_id=recipe_id))
@app.route('/add_comment_to_recipe/<recipe_id>', methods=['POST'])
def add_comment_to_recipe(recipe_id):
    recipes = mongo.db.recipes
    
    recipes.update(
        {'_id': ObjectId(recipe_id)},
        {
             '$push':{'comments': request.form.get('comment')}
        }, upsert=True)
    return redirect(url_for('show_recipe', recipe_id=recipe_id))

@app.route('/update_recipe/<recipe_id>', methods=['POST'])
def update_recipe(recipe_id):
    recipes = mongo.db.recipes
    recipes.update({'_id': ObjectId(recipe_id)},
    {
        'recipe_name':request.form.get('recipe_name'),
        'prep_time':request.form.get('prep_time'),
        'cook_time':request.form.get('cook_time'),
        'ingredients':request.form.get('ingredients'),
        #'cuisine':request.form.get('cuisine'),
        'method_steps':request.form.get('method_steps'),
        'tools_used':request.form.get('tools_used'),
        'image_link':request.form.get('image_link')
    })
    return redirect(url_for('get_top_recipes'))

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