import sys, threading

def run():
	debug_file = open('input', 'r')
	for line in debug_file:
		try:
			e = entry(line)
		except Exception as e:
			print e

def main(): 
	server = HTTPServer(('localhost', 8080), handler)
	print 'Starting httpd...'
	server.serve_forever()

if __name__ == '__main__': 
	debug = 'debug' in sys.argv
	main()
	if debug: 
		t = threading.Thread(target=run)
		t.daemon = True
		t.start()
		raw_input()
