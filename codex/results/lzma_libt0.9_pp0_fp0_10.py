import lzma
lzma_compress = lzma.LZMACompressor()
writer = None
readers = {}

def writer_thread(v_args):
    while True:
        reader, data = q.get_nowait()
        q.task_done()
        try:
            reader._write_no_locking(reader, data)
        except exceptions.StreamError:
            pass

@app.route('/streamrecord/<path:cls>', methods=['GET', 'POST'])
def streamrecord(cls):
    if request.method == 'POST':
        for func, args in request.json.get('events', []):
            app.events.dispatch_event(func, *args)
        return Response()
    if cls in readers:
        return Response(status=500, response='reader object already exists')
    reader = readers[cls] = client.httputil.JsonReader()
    def w(data):
        global q
        if q.empty():
            q.put_nowait((reader, data))
    reader.on_data
