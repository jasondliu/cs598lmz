import threading
threading._DummyThread._Thread__stop = lambda x: 42
import sys

class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write("Hello, world!")
