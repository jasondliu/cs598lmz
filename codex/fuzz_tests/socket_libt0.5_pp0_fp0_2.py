import socket
import time
import threading
import signal
import sys
import os

HOST = ''
PORT = 8888

def signal_handler(signal, frame):
	print "Exiting..."
	os.kill(os.getpid(), signal.SIGKILL)

signal.signal(signal.SIGINT, signal_handler)

def client_thread(clientsocket):
	"""
		Main client thread
	"""
	while True:
		try:
			data = clientsocket.recv(1024)
			if data:
				clientsocket.send(data)
			else:
				clientsocket.close()
				break
		except:
			clientsocket.close()
			break

def main():
	"""
		Main server thread
	"""
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.setsockopt(socket.SOL_SOCKET, socket.SO_RE
