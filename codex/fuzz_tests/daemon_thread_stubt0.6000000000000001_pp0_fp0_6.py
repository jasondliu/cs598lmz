import sys, threading

def run():
	if(len(sys.argv) != 2):
		print("usage: python3 client.py <port>")
		sys.exit(1)
	
	host = 'localhost'
	port = int(sys.argv[1])
	
	#setup sockets
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, port))
	
	#send welcome message
	s.sendall(b'Hello, world')
	
	#recieve response
	data = s.recv(1024)
	print('Received', repr(data))
	
	#close connection
	s.close()
	
	
	
threading.Thread(target=run).start()
