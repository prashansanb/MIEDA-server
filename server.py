from flask import Flask, request

app = Flask(__name__)

@app.route("/android", methods=['POST'])
def getJSONData():
    data_json = request.get_json() # get JSON object
    ''' @TODO:
    1. get base64 String
    2. parse base64 string and convert to image
    3. implement sentiment analysis
    4. return results
    '''
    return "Call Successful"
