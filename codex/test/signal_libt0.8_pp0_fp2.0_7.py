import signal
signal.signal(signal.SIGTERM, main.signal_handler)

# Create the web server and the CGI handler.
server = HTTPServer(('', 8000), CGIHTTPRequestHandler)
server.serve_forever()
