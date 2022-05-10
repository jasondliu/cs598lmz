import sys, threading

def run():
	server = Server()
	server.run()

def test():
	threading.Thread(target=run).start()
	client = Client()
	client.run()

if __name__ == '__main__':
	if len(sys.argv) > 1:
		if sys.argv[1] == '--test':
			test()
		elif sys.argv[1] == '--server':
			run()
		else:
			print 'Invalid argument. Valid arguments are: --test, --server'
	else:
		print 'No arguments provided. Valid arguments are: --test, --server'
