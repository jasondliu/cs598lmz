import socket
# Test socket.if_indextoname
if __name__ == '__main__':
	if 'h1-eth0' not in socket.if_indextoname(3):
		sys.exit(-1)
