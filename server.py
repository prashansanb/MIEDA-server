import base64
from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route("/android", methods=['POST'])
def getJSONData():
    data_json = request.get_json() # get JSON object
    ''' @TODO:
    1. get base64 String - Done
    2. parse base64 string and convert to image - Done
    3. implement sentiment analysis
    4. return results
    '''
    base64String = data_json['imgBase64']
    filename = get_file_name()

    with open(filename, 'wb') as image:
        image.write(base64.b64decode(base64String))

    analysis = emotion_api(filename)

    return jsonify(analysis)


def get_file_name():
    return datetime.now().strftime('IMG_%Y%m%d_%H%M%S.jpg')

def emotion_api(filename):
    '''@TODO: Implement analysis'''
    analyzed_data = {"null": "null"}
    return analyzed_data
