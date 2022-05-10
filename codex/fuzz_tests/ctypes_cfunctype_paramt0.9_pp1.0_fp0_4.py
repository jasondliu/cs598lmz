import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.POINTER(ctypes.c_int),
                         ctypes.c_int, ctypes.c_int, ctypes.c_int)

m = FUNTYPE(call)


@app.route('/cfun')
def cfun():
    start = int(request.args.get('start'))
    count = int(request.args.get('count'))
    tokens = m(start, count, arr)
    return jsonify([tokens[i] for i in xrange(0, count)])


@app.route('/dataset')
def dataset():
    start = int(request.args.get('start'))
    count = int(request.args.get('count'))
    return jsonify(arr[start:start+count])


@app.route('/report')
def report():
    return jsonify([{'label': k, 'count': v} for (k, v) in sorted((count(k) for k in set(arr)),
                                                                  key=lambda x: x[1],
                                                
