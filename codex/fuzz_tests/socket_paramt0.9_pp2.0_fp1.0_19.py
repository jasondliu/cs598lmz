import socket
socket.if_indextoname(4)
#'enp4s0'
socket.if_nameindex()[0]
#(1, 'lo')
socket.if_nametoindex('lo')
#1
socket.if_nameindex()[1][1]
#'lo'
socket.if_nametoindex('lo')
#1
socket.if_indextoname(4)
#'enp4s0'

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
localIP = socket.gethostbyname(socket.gethostname())
s.connect((localIP, 9090))
print(s.getsockname()[0])
s.close()

HOST = ''   # Symbolic name, meaning all available interfaces
PORT = 9090  # Arbitrary non-privileged port
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.bind((HOST, PORT))
	s.listen(5)
	conn, addr = s.accept()
	with conn
