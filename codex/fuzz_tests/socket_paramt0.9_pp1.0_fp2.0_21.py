import socket
socket.if_indextoname(3)

try:
	eths = ('eth0', 'eth1')
	s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW)
	s.bind((eths[0], socket.SOCK_RAW))
	for x in range(256):
		print(x)
		socket.if_indextoname(x)
except:
	print(1)
