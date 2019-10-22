# Data Centric Development Milestone Project #
This project is an online database for recipes, called Clever Cooking. Upon arrival to the site, the user will see a list of top recipes, ordered by the amount of ‘likes’ they have. From this home page the user can also search for existing recipes based on dietary requirements.
Users can quickly see from a glance the image of the recipe, the name of it, and the number of likes it has.
You can click on the recipe to get a quick view of it, and then also click ‘View full recipe’, which brings you to the actual page with the recipe on it.
Once the user clicks on the full recipe, they have the ability to see different aspects such as the Cooking time, the Calories, tools used and the method of cooking.
Comments are available here also, and the user may post their own comment, which will appear underneath.
## UX ##
The objective of the site is to find, view and edit recipes online. This site makes it easy for the user to upload their own recipes and view more. 
The homepage contains all that a user would need from the perspective of uploading and viewing recipes.

## Data ##
For this, I used MongoDB as my database. I structured it with collection called recipes, with values such as below:
{"_id":{"$oid":"5d5015614e88b888f2567f63"},"recipe_name":"Stir fry","prep_time":"10 mins","cook_time":"20 mins","ingredients":"Vegetables, noodles","method_steps":"open packet of food, cook the food, eat the food","tools_used":"wok","likes":{"$numberInt":"4"},"image_link":"https://d1doqjmisr497k.cloudfront.net/-/media/mccormick-us/recipes/mccormick/s/800/stir_fry_vegetables_800x800.jpg"}

So each recipe has its own document, with unique id and properties.

In order to do comments, I chose to create a new collection called comments. These entries contain their own unique id but also the id of the recipe they are related to. An entry looks like this: {"_id":{"$oid":"5dab4593cdcc0854ed2b43da"},"username":"burgerLover","comment":"best burger ever","_recipe_id":{"$oid":"5d4eb2bc1c9d440000c86cc0"}}


### User stories: ###
1. As a baker, I want to upload my new cake recipe.
2. As a potential baker, I want to view a cake recipe.
3. As a site visitor I want to show appreciation of other peoples recipes.
4. As a coeliac, I want to view all gluten-free recipes.
5. As a vegetarian, I want to share my meat-less dishes.
   
## Features  ##
### Existing Features ###
- Home page - Allows users to get an overview of the top rated recipes on the site
- Search bar - Allows users to search for recipes based on dietary requirements
- Quick view - Allows users to view a recipe quickly instead of viewing the entire recipe on a new page.
- Likes - Allows a user to rate the recipe. This will affect the order the recipes appear in, and letting the better recipes appear first for the homepage.
- Recipe page - Allows users to view everything about the recipe
- Comment section - Lets users make comments on recipes under a username, for other users to see
- Edit recipe section - Allows users to make changes to the existing recipe
- Delete - Allows user to Delete recipe

### Features Left to Implement ###
- Extending search to be able to search by ingredients and not just by dietary needs
- Pagination, where only the top 15 recipes are shown at once
- Making the site more mobile friendly, where recipes become stacked
- User accounts, where users can post recipe’s under their own name
- Users may become rated based on their recipe ratings
- Users may upload images instead of using links
## Technologies Used ##
 HTML, CSS, Flask, jQuery
## Testing ##
- All testing for this project was done manually due to time constraints. Ideally the backend functionality would have been tested with automated scripts.
I used chrome developer tools to test how the site works on different size screens

### Scenarios ###
Create new Recipe
- Try to submit a recipe without filling out all of the forms
Add a comment
- Try to add a comment without providing a username
- Try add comment without putting text in comment field
Delete a Recipe
Edit a Recipe


## Deployment ##
This application is deployed via Heroku: https://online-recipe-cookbook-flask.herokuapp.com/
## Credits ##

## Content ##
 Content taken from bbcgoodfood, and google
## Media ##
The photos used in this site were obtained from google
## Acknowledgements ##
 

