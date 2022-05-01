from flask import Flask
from flask import request
from pymongo import MongoClient
import certifi
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
client = MongoClient("mongodb+srv://tinaah:OgJ3sWDC8Oc03WUp@plextech-tinaah-project.wcszi.mongodb.net/myFirstDatabase?retryWrites=true&w=majority", tlsCAFile=certifi.where())
db_user = client.users
user_collection = db_user.user_collection
db_review = client.reviews
review_collection = db_review.review_collection

@app.route("/reviews/<cafe_type>/<username>", methods=["GET"])
def reviews_get(cafe_type, username):
    if not user_collection.find_one({"username" : username}):
        return {"message": "user does not exists!"}, 400
    reviews = review_collection.find({"username" : username, "cafe_type" : cafe_type})
    output = []
    for data in reviews:
        temp = {
            "username": data['username'],
            "taste_rating": data['taste_rating'],
            "visual_rating": data['visual_rating'],
            "nutrition_rating": data['nutrition_rating'],
            "cafe_type" : data['cafe_type'],
            "review" : data['review']
        }
        output.append(temp)
    return {"result": output}, 200

@app.route("/reviews", methods=["POST"])
def reviews_post():
    data = request.json
    if user_collection.find_one({"username" : data['username'], "cafe_type" : data['cafe_type']}):
        return {"message": "review for this cafe is already posted by this user"}, 400
    post = {
            "username": data['username'],
            "taste_rating": data['taste_rating'],
            "visual_rating": data['visual_rating'],
            "nutrition_rating": data['nutrition_rating'],
            "cafe_type" : data['cafe_type'],
            "review" : data['review']
        }
    post_id = review_collection.insert_one(post).inserted_id
    print(str(post_id))
    return {"message": "review added successfully"}, 200

app.run(port=5001, debug=True)