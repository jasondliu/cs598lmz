import socket
socket.if_indextoname(socket.if_nametoindex('eth0'))
socket.gethostbyname('localhost')
 
import socket
def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]
get_ip_address()

# Creating a socket
socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Binding to a socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.bind(('127.0.0.1', 1234))

# Connecting to a socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('127.0.0.1', 1234))

# Closing a socket
mysock.shutdown(socket.SHUT_RDWR)

# The TCP three-way handshake

# Open a socket
