import sys, threading

def run():
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.bind(('', PORT))
	server.listen(5)
	print 'TCP is listening on port: ', PORT

	while True :
		connection, address = server.accept()
		print 'Client connected: ', address
		while True:
			data = connection.recv(1024)
			if data == '': break
			print 'Received: ', data
		connection.close()
		print 'Client disconnected.'

if __name__ == '__main__':
	PORT = 3000
	run()
