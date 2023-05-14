from flask import Flask, request, jsonify
from flask_ngrok import run_with_ngrok
from flask_cors import CORS
import base64
import json
import pyrebase
from google.cloud import firestore
import os
#from model import get_pred, m
from flask_cors import CORS, cross_origin

app = Flask(__name__)
app.config['CORS_HEADERS']='Content-Type'
CORS(app, expose_headers='Authorization')
run_with_ngrok(app)
app.debug=True

with open('config.json') as json_file:
    config = json.load(json_file)

firebase = pyrebase.initialize_app(config)
db = firebase.database()

@app.route("/get_img", methods = ['GET', 'POST'])
def recieve():
  data = request.get_json()

  image = data['image']
  time = data['time']

  string_bytes = bytes(str(image), 'utf-8')

  with open(f"img.jpg", "wb") as fh:
    fh.write(base64.decodebytes(string_bytes))

  db.child('data/').update(
                {time: {
                    'img': str(image),
                    'whoIsIt': "me"
                }}
            )

  return "a"


if __name__ == "__main__":
  app.run()