import socket
import select
import sys
import threading
import time

def prompt():
	sys.stdout.write('<You> ')
	sys.stdout.flush()

if __name__ == "__main__":
	if(len(sys.argv) < 3):
		print("Usage: python3 client.py <hostname> <port>")
		sys.exit()

	host = sys.argv[1]
	port = int(sys.argv[2])

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.settimeout(2)

	try:
		s.connect((host, port))
	except:
		print("Unable to connect")
		sys.exit()

	print("Connected to remote host. You can start sending messages")
	prompt()

	while 1:
		socket_list = [sys.stdin, s]

		# Get the list sockets which are readable
		read_sockets, write_sockets, error_sockets
