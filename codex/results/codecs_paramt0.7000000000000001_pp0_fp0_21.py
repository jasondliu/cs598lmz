import codecs
codecs.register_error('surrogate_or_unknown', codecs.UTF8_REPLACE)

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/search', methods=['GET'])
def search():
    # if not request.json:
    #     abort(400)
    if 'q' not in request.args:
        abort(400)
   
    query = request.args['q']
    print query
    results = search_request(query)
    print results
    return jsonify(results=results)

def search_request(query):
    url = 'http://api.twitter.com/1/search.json'
    params = {'q': query}
    r = requests.get(url, params=params)
    r.encoding = 'ascii'
    return r.json

if __name__ == '__main__':
    app.run(debug=True)
