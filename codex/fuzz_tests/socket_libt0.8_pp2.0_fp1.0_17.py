import socket
import time

# TCP_IP = '192.168.1.1'
# TCP_IP = '127.0.0.1'
# TCP_IP = '192.168.0.100'
TCP_IP = '192.168.43.65' #WIFI
TCP_PORT = 5005
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.settimeout(1.0)

try:
	while True:
		print('\nEnter Command:')
		MESSAGE = input()
		if MESSAGE == 'q':
			break
		MESSAGE = MESSAGE + '\n'
		s.send(MESSAGE.encode('ascii'))
		data = s.recv(BUFFER_SIZE)
		print('Received data: ' + data.decode('ascii'))
		if '
