import sys, threading

def run():
	threading.Thread(target=run_server).start()
	threading.Thread(target=run_client).start()
	
def run_server():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind(('localhost', 0))
	s.listen(1)
	conn, addr = s.accept()
	print('server:', conn.recv(1024))
	conn.close()
	print('server: done')
	
def run_client():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(('localhost', 8080))
	s.sendall(b'Hello, world')
	s.close()
	print('client: done')

if __name__ == '__main__':
	run()
