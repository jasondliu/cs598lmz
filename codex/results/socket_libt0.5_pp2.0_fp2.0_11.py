import socket
import urllib.parse

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    query = request.args.get('q')
    scheme = request.args.get('scheme')
    host = request.args.get('host')
    port = int(request.args.get('port'))
    path = request.args.get('path')
    params = request.args.get('params')
    fragment = request.args.get('fragment')
    return render_template('result.html', query=query, scheme=scheme, host=host, port=port, path=path, params=params, fragment=fragment)

@app.route('/search_url')
def search_url():
    query = request.args.get('q')
    url = request.args.get('url')
    return render_template('result_url.html', query
