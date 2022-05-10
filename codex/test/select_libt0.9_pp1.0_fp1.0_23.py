import selectors
import queue
import threading
import socket
import time
import multiprocessing
import urllib.parse
import sys
import configparser

HOST = '127.0.0.1'
PORT = 8080
BUF_SIZE = 1024
MAX_CONNECTIONS = 5
MAX_RECV = BUF_SIZE * MAX_CONNECTIONS
PROCESS = 4

PID = os.getpid()

TOTAL_REQ = 0
TOTAL_CP = 0
AVG_TIME = 0
START = time.time()

def handle_client(client_socket, total_byte, t1):
	print('ready to handle client request')
	num = client_socket.recv(1024)
	# print('received num: ', num)
	global TOTAL_REQ
	TOTAL_REQ += 1
	if not num:
		print('closing client socket')
		with lock:
			client_socket.close()
	else:
		num = int(num)
