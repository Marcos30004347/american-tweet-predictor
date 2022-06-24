from flask import Flask, request, jsonify

import pickle

import requests

from os import getcwd

import os

version = os.environ.get('MODEL_VERSION')

def load_model(version):
    url = "https://raw.github.com/Marcos30004347/tweet_prediction_models/main/" + version
    directory = getcwd()
    filename = directory + "/" + version
    req = requests.get(url)
    open(filename,'wb').write(req.content)
    return pickle.load(open(filename, 'rb'))

model = load_model(version)
    
app = Flask(__name__)

@app.route("/api/american", methods=["POST"])
def api_american():
    content = request.json
    
    is_american = model.predict([content['text']])
  
    return jsonify({
        "is_american": str(is_american[0]),
        "version": str(version),
        "model_date": "23/06/2022"
    })
  