from flask import Flask
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

app.run(host='0.0.0.0', port=5000)