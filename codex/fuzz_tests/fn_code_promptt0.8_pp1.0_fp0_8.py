fn = lambda: None
# Test fn.__code__ changes in Python 3.7
app.config['TESTING'] = True


@app.route('/')
def hello_world():
    return '{"statusCode": 200, "body": "Hello World!"}'


@app.route('/echo', methods=['POST'])
def echo():
    return jsonify(request.get_json())


@app.route('/echo-headers', methods=['POST'])
def echo_headers():
    return jsonify(dict(request.headers)), 200, {'X-Echo-Header': 'Test'}


@app.route('/echo-path/<path_param>', methods=['POST'])
def echo_path(path_param):
    return jsonify({'path_param': path_param})


@app.route('/echo-query', methods=['GET'])
def echo_query():
    return jsonify(dict(request.values))


@app.route('/echo-path-query/<path_param>', methods=['GET'])
def echo_path_query(path_
