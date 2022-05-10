import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

class WebServer(object):
	def __init__(self, port=8080):
		self.port = port
		self.server = None

	def start(self):
		self.server = ThreadedHTTPServer(('', self.port), WebHandler)
		self.server.serve_forever()

	def stop(self):
		self.server.shutdown()

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
	"""Handle requests in a separate thread."""

class WebHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		self.send_response(200)
		self.send_header('Content-type', 'text/html')
		self.end_headers()
		self.wfile.write(bytes("<html><head><title>Title goes here.</title></head>", "utf-8"))
		self.wfile.write(bytes("
