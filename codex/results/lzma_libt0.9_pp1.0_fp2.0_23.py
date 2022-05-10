import lzma
lzma.__all__

import zlib
zlib.crc32()

import sysv_ipc
help(sysv_ipc.MessageQueue)



# --- BaseHTTPServer ---
import BaseHTTPServer

class HttpServer(object):
    def __init__(self, addr=('127.0.0.1', 80)):
        self.addr = addr
        self.httpd = BaseHTTPServer.HTTPServer(self.addr, self.HttpHandler)

    class HttpHandler(BaseHTTPServer.BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'get receive')
            return

        def do_POST(self):
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'post receive')
            return

    def run(self):
        while True:
            self.httpd.handle_request()

# in main.py
#
