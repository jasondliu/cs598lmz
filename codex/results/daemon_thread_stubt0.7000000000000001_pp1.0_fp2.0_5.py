import sys, threading

def run():
    # set up input/output streams
    sys.stdout = sys.stderr = open('/dev/null', 'w')
    sys.stdin = open('/dev/null', 'r')
    # run the server on port 8000
    #httpserver.test(HandlerClass=MyHandler, ServerClass=HTTPServer, port=8000)
    httpserver.test(HandlerClass=MyHandler, ServerClass=http.server.ThreadingHTTPServer, port=8000)

if __name__ == '__main__':
    # start the server in a thread
    threading.Thread(target=run).start()
    # make a few requests
    for i in range(3):
        urllib.request.urlopen('http://localhost:8000/')
