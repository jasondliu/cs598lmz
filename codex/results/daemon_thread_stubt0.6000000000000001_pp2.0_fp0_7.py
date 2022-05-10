import sys, threading

def run():
	global PORT
	HOST = 'localhost'
	PORT = 8001
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((HOST, PORT))
	s.send('Hello, world')
	data = s.recv(1024)
	s.close()
	print 'Received', repr(data)

if __name__ == '__main__':
	threading.Thread(target=run).start()
	threading.Thread(target=run).start()
	threading.Thread(target=run).start()
	threading.Thread(target=run).start()
	threading.Thread(target=run).start()
	threading.Thread(target=run).start()
	threading.Thread(target=run).start()
	threading.Thread(target=run).start()
	threading.Thread(target=run).start()
	threading.Thread(target=run).start()
	threading.Thread(target=run).start()
	threading.Thread(target=
