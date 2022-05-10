import socket
from struct import pack

def getAddr(host, port):
	return (socket.gethostbyname(host), port)

def getSocket(port):
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.bind(('0.0.0.0', port))
	return sock

def send(sock, host, port, data):
	sock.sendto(data, (socket.gethostbyname(host), port))

def recv(sock):
	return sock.recvfrom(4096)

def recvfrom(sock, host, port):
	return recv(sock)[0]

def recvfrom_timeout(sock, timeout=1):
	sock.setblocking(0)
	ready = select.select([sock], [], [], timeout)
	if ready[0]:
		return sock.recvfrom(4096)
	else:
		return (None, None)

def recv_timeout(sock,
