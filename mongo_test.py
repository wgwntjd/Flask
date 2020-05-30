from pymongo import MongoClient
from flask import Flask, request, redirect, url_for, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/mongo', methods=['POST'])
def mongoTest():
    client = MongoClient('mongodb://localhost:27017/')
    db = client.sample
    collection = db.user
    results = collection.find()
    client.close()
    return render_template('mongo.html', data=results)

if __name__ == '__main__':
    app.run(debug=True)