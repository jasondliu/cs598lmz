import threading
threading.stack_size(64*1024)

def main():
	server = HTTPServer(('', 8080), Serv)
	print('started httpserver...')
	server.serve_forever()

