from flask import Flask
from flask import jsonify
from flask_pymongo import PyMongo

from mongoengine_jsonencoder import JSONEncoder
from utilLog import logger
logger.info("app.py main method")
app = Flask(__name__)
logger.info("JSON ENCODER FOR JSON")
app.json_encoder = JSONEncoder

app.config['MONGO_DBNAME'] = 'imdb'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/imdb'

mongo = PyMongo(app)


@app.route('/', methods=['GET'])
def get_all_movies():
  movie = mongo.db.movies
  logger.debug(movie)
  result = []
  for m in movie.find():
    logger.info("collection appending")
    result.append({ "_id" : m["_id"], "99popularity" : m["99popularity"],"director": m["director"],"genre": m["genre"],"imdb_score" : m["imdb_score"], "name":m["name"]})
  logger.info("Json object serilazation")
  return jsonify({"imdb_movies" : result})

if __name__ == '__main__':
    app.run(debug=True)
