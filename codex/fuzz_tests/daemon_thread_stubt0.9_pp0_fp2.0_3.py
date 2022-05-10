import sys, threading

def run():
	server = BaseHTTPServer.HTTPServer(
		('', 8000),
		SimpleHTTPServer.SimpleHTTPRequestHandler
	)
	server.serve_forever()

thread = threading.Thread(target=run)
thread.start()

import IPython; IPython.embed()
</code>

