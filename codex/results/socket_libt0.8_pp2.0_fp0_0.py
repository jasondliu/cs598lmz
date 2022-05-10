import socket
import time
from socketserver import ThreadingMixIn
from http.server import BaseHTTPRequestHandler, HTTPServer

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
	pass


class MyServer(BaseHTTPRequestHandler):
	def do_HEAD(self):
		self.send_response(200)
		self.send_header('Content-type', 'text/html')
		self.end_headers()

	def do_GET(self):
		self.do_HEAD()
		self.wfile.write(bytes("<html><head><title>Title goes here.</title></head>", "utf-8"))
		self.wfile.write(bytes("<body><p>This is a test.</p>", "utf-8"))
		self.wfile.write(bytes("<p>You accessed path: {}</p>".format(self.path), "utf-8"))
		self.wfile.write(bytes("</body></html>", "utf-8"))
	
	def do_POST(self):
	
