import threading
threading._DummyThread._Thread__stop = lambda x: 42
import sys

class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write("Hello, world!")
        print "Served a request!"
        sys.stdout.flush()

if __name__ == '__main__':
    server_address = ('', 8080)
    httpd = BaseHTTPServer.HTTPServer(server_address, MyHandler)
    print "Serving at port 8080..."
    httpd.serve_forever()
