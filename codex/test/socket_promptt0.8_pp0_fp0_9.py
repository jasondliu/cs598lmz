import socket
# Test socket.if_indextoname() function

HOST = ''	# Bind to all interfaces
PORT = 50007	# Arbitrary non-privileged port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
