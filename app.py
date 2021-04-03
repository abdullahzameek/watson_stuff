import re
import flask
import requests
import json
from flask_cors import CORS
from flask import request

app = flask.Flask(__name__)
CORS(app)



url = 'https://gateway-lon.watsonplatform.net/natural-language-understanding/api/v1/analyze'
user = "apiKey"
pw = "NYrce6xil-76pPdybo0xaNLtf2u2a1iM7zrQlKDppETF"


@app.route("/getSentiment", methods=['POST', 'GET'])
def getSentiment():
    print('here is the request json')
    print(request.json)
    payload_text = request.json['text']

    payload = {
        'version': '2020-08-01',
        'features': 'sentiment',
        'text':payload_text
    }
    
    resp = requests.get(url, params=payload, auth=(user, pw))
    content = resp.content.decode()
    content2 = json.loads(content)
    # print(content2['sentiment']['document'])
    return json.dumps(content2['sentiment']['document'])


@app.route("/getEmotion", methods=['POST', 'GET'])
def getEmotion():
    print('here is the request json')
    print(request.json)
    payload_text = request.json['text']

    payload = {
        'version': '2020-08-01',
        'features': 'emotion',
        'text':payload_text
    }
    
    resp = requests.get(url, params=payload, auth=(user, pw))
    content = resp.content.decode()
    content2 = json.loads(content)
    print(content2['emotion']['document']['emotion'])
    return json.dumps(content2['emotion']['document']['emotion'])




