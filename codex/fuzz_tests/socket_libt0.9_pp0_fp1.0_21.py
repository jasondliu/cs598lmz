import socket
import threading
import urllib
hello = 'hello'
header = 'HTTP/1.1 200 OK\r\ncontent-type: text/html\r\n'
header += 'content-length: %d\r\n\r\n' % len(hello)

def handle(client):
	print 'handle:', client
	#print client.recv(1024)
	print client.recv(1024)
	client.send(header)
	client.send(hello)
	client.close()

def loop_run():
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	server.bind(('0.0.0.0', 8080))
	server.listen(128)
	while True:
		client, addr = server.accept()
		handle(client)
		print 'client', client, 'close'

def thread_run():
	server =
