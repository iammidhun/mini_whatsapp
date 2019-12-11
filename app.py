from flask import Flask
from flask_mongoengine import MongoEngine
from flask_restful import Resource, Api
from pymongo import MongoClient
from flask_login import login_manager

app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'hi'

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.config['MONGODB_SETTINGS'] = {
	'db': 'whatsapp',
	'host': 'localhost',
	'port': 27017
}
db = MongoEngine(app)
api = Api(app)

if __name__ == "__main__":
	app.run(debug=True)
	