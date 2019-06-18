from flask import Flask
from flask import request
from Classifier import Classifier
app = Flask(__name__)

@app.route('/hackaton')
def index():
    query = request.args.get('query')
    classifier = Classifier()
    return classifier.classify(query)


app.run(host='0.0.0.0', port=5000)