import mmap
import sys
from flask import Flask, request, render_template
from roman import fromRoman

app = Flask(__name__, static_folder='static', static_url_path='')

@app.route('/')
def root():
	return app.send_static_file('index.html')

@app.route('/answer.json')
def answer():
	value = request.args.get('value', default = '')
	state = request.args.get('state', default = '')
	res = ordinal_from_value(value)
	res['state'] = state
	print res
	return res

@app.route('/submit', methods=['GET'])
def submit():
	answers = request.args.get('answers', default = '')
	notes = request.args.get('notes', default = '')
	state = request.args.get('state', default = '')
	with open('answers/%s-%s.txt' % (answers, state), 'w') as answers_log:
