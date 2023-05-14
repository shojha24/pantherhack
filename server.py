from flask import Flask, request, jsonify
from flask_ngrok import run_with_ngrok
from flask_cors import CORS
import base64
import json
import pyrebase
import os
from PIL import Image#from model import get_pred, m
from flask_cors import CORS, cross_origin
import tensorflow as tf
from tensorflow import keras
import numpy as np

app = Flask(__name__)
app.config['CORS_HEADERS']='Content-Type'
CORS(app, expose_headers='Authorization')
run_with_ngrok(app)
app.debug=True

with open('config.json') as json_file:
    config = json.load(json_file)

firebase = pyrebase.initialize_app(config)
db = firebase.database()

model = tf.keras.models.load_model("celebrity_classification_TFL.h5")

def get_and_process():
    img = Image.open('img.jpg')
    img1 = img
    """Resize image to appropriate shape for model."""
    img = img.resize((150,150))
    """Convert img to numpy array,rescale it,expand dims and check vertically."""
    x = tf.keras.preprocessing.image.img_to_array(img)
    x = x / 255.0
    x = np.expand_dims(x,axis = 0)
    img_tensor = np.vstack([x])
    return img1,img_tensor

@app.route("/get_img", methods = ['GET', 'POST'])
def recieve():
  data = request.get_json()

  image = data['image']
  time = data['time']

  string_bytes = bytes(str(image), 'utf-8')

  with open(f"img.jpg", "wb") as fh:
    fh.write(base64.decodebytes(string_bytes))
  
  img, img_tens = get_and_process()
  prediction = model.predict(img_tens)

  classes = ['Angelina Jolie', 'Brad Pitt', 'Denzel Washington', 'Hugh Jackman', 'Jennifer Lawrence', 'Johnny Depp', 'Kate Winslet', 'Leonardo DiCaprio', 'Megan Fox', 'Natalie Portman', 'Nicole Kidman', 'Robert Downey Jr', 'Sandra Bullock', 'Scarlett Johansson', 'Tom Cruise', 'Tom Hanks', 'Will Smith']
  print(f"Prediction is : {classes[np.argmax(prediction)]}")

  if classes[np.argmax(prediction)] in ["Brad Pitt", 'Denzel Washington', "Jennifer Lawrence", "Johnny Depp", "Tom Cruise"]:
     whoIsIt = classes[np.argmax(prediction)]
  else:
     whoIsIt = "False"

  db.child('data/').update(
                {time: {
                    'img': str(image),
                    'whoIsIt': whoIsIt
                }}
            )

  return classes[np.argmax(prediction)]


if __name__ == "__main__":
  app.run()