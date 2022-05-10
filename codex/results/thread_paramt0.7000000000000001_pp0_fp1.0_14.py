import sys, threading
threading.Thread(target=lambda: __import__('webbrowser').open('http://localhost:8081/')).start()
print "Server is running at http://localhost:8081/"
try:
	httpd.serve_forever()
except KeyboardInterrupt:
	print "Server stopped"
