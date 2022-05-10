import sys, threading

def run():
    httpd = make_server('127.0.0.1', 8000, serve)
    httpd.serve_forever()

def serve(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    host = environ.get('HTTP_HOST')
    path = environ.get('PATH_INFO')
    query = environ.get('QUERY_STRING')
    accept_language = environ.get('HTTP_ACCEPT_LANGUAGE')
    return ["%s %s %s %s" % (host, path, query, accept_language)]

t = threading.Thread(target=run, args=())
t.start()
</code>
When I <code>python test.py</code> and hit it with a browser, I can see the result and it works fine but my terminal window is filled with messages:
<code>127.0.0.1 - - [23/Apr/2016 12:36:26] "GET / HTTP/1.1" 200 22 127.0.
