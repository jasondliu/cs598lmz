import sys, threading

def run():
    # Set up the server
    from wsgiref.simple_server import make_server
    srvr = make_server('localhost', 8051, application)
    srvr.serve_forever()

def application(environ, start_response):
    status = '200 OK'
    output = 'Hello World!'

    response_headers = [('Content-type', 'text/plain'),
                        ('Content-Length', str(len(output)))]
    start_response(status, response_headers)

    return [output]

thread = threading.Thread(target=run)
thread.start()
