import sys, threading

def run():
    gfw.run(port=8000)

if env == "pro":
    print "pro env"
    gfw = WSGIServer(('0.0.0.0', 80), app, log=None, handler_class=WebSocketHandler)
    thread = threading.Thread(target=run, args=())
    thread.setDaemon(True)
    thread.start()
    gfw.serve_forever()

elif env == "dev":
    gfw = make_app()
    gfw.run(port=8000, debug=True)
else:
    sys.exit(0)
