import socket

# Address
HOST = ''
PORT = 8001
ADDR = (HOST,PORT)
BUFSIZE = 4096

# Configure socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(ADDR)
s.listen(5)

