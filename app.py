from flask import Flask, request, jsonify

import pickle

import requests

from os import getcwd

from datetime import datetime

import os

model_version = os.environ.get('MODEL_VERSION')
server_version = os.environ.get('SERVER_VERSION')

def load_model(version):
    url = "https://raw.github.com/Marcos30004347/tweet_prediction_models/main/" + version
    date = datetime.now().timestamp()
    directory = getcwd()
    filename = directory + "/" + version
    req = requests.get(url)
    open(filename,'wb').write(req.content)
    return pickle.load(open(filename, 'rb'))

model_data = load_model(model_version)

model = model_data['model']

model_date = datetime.utcfromtimestamp(int(model_data['model_date'])).strftime('%Y-%m-%d %H:%M:%S')

app = Flask(__name__)

@app.route("/api/american", methods=["POST"])
def api_american():
    content = request.json
    
    is_american = model.predict([content['text']])
  
    return jsonify({
        "is_american": str(is_american[0]),
        "version": str(server_version),
        "model_date": str(model_date)
    })
  