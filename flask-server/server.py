from flask import Flask
from dotenv import dotenv_values
from pprint import pprint
from flask_pymongo import PyMongo
from flask import jsonify
from flask import request
import json
import spacy
from bson import json_util
config = dotenv_values(".env")

class RecipeEncoder(json.JSONEncoder):
    def default(self, obj):
        
        if isinstance(obj, Recipe):
            return { 'name' : obj.name,  
                     'link' : obj.link ,
                     'ingredients' : obj.ingredients,
                     'directions' : obj.directions}

        return json.JSONEncoder.default(self, obj)

class Recipe:
    def __init__(self, name, link, ingredients, directions):
        self.name = name
        self.link = link
        self.ingredients = ingredients
        self.directions = directions
        self.cleared_name = ' '.join(self.name.split('-'))

nlp = spacy.load("en_core_web_md") 
app = Flask(__name__)
app.config["MONGO_URI"] = config['MONGO_URI']
app.json_encoder = RecipeEncoder
mongo = PyMongo(app)

@app.route("/recipes")
def recipes():
    all_recipes = [
        Recipe(x['link'].split('/')[-2],
            x['link'], x['ingredients'], 
            x['directions'])
        for x in mongo.db.RecipeList.find({})
    ]
    return jsonify(all_recipes)

@app.route("/recipe/filter/")
def recipes_filter():
    #search_terms = request.form.get('search')
    search_terms = request.args.get('search')
    processed_search = nlp(search_terms)
    all_recipes_by_name = [
        [nlp(' '.join((x['link'].split('/')[-2]).split('-'))),
        x['link']
        ]
        for x in mongo.db.RecipeList.find({})
    ]

    ordered_recipes = sorted(all_recipes_by_name,
                            key = lambda x: x[0].similarity(processed_search),
                            reverse = True
                            )[:10]

    query_recipes = []
    for recipe in ordered_recipes:
        p = mongo.db.RecipeList.find_one({'link' : recipe[1]})
        query_recipes.append(Recipe(p['link'].split('/')[-2],
                                    p['link'],
                                    p['ingredients'],
                                    p['directions']))

    return jsonify(query_recipes)

@app.route("/members")
def members():
    return {"members": ["Member1", "Member2", "Member3"]}

if __name__ == "__main__":
    app.run(debug=True)