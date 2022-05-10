import socket
import threading
import struct
import time
import sys

def main():
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		s.bind(('', 8080))
		s.listen(10)
	except socket.error as message:
		if s:
			s.close()
		print("Could not open socket: " + str(message))
		sys.exit(1)

	while True:
		conn, addr = s.accept()
		threading.Thread(target=responder, args=(conn, addr)).start()

def responder(conn, addr):
	response = "HTTP/1.1 200 OK\nConnection: close\nServer: Python\nContent-Length: 13\n\nHello World!"
	conn.send(response)
	conn.close()

