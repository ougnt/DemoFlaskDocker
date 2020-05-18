from flask import Flask
from flask import send_file
import os.path

app = Flask(__name__)

def get_file(file_name):
	return open(os.path.join(os.path.abspath(os.path.dirname(__file__)), file_name), 'r').read()

@app.route('/')
def home():
	return get_file('view/home.html')

@app.route('/js/<path:path>')
def get_js_sript(path):
	return get_file('scripts/' + path)

@app.route('/images/<path:path>')
def get_image(path):
	return send_file('photo/' + path, mimetype='image/gif')

app.run(host='0.0.0.0', port=5000)