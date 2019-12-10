from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'hi'

if __name__ == "__main__":
	app.run()
	
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.config['MONGODB_SETTINGS'] = {
	'db': 'whatsapp',
	'host': 'localhost',
	'port': 27017
}