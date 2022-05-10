import sys, threading

def run():
	try:
		server.serve_forever()
	except KeyboardInterrupt:
		print('bye')
		sys.exit()

if __name__ == '__main__':
	host = '192.168.0.100'
	port = 8080

	server = socketserver.TCPServer((host, port), MyTCPHandler)

	t = threading.Thread(target=run)
	t.daemon = True
	t.start()
	while True:
		try:
			msg = input('enter a msg:')
			if msg == "exit":
				sys.exit()
		except:
			sys.exit()
