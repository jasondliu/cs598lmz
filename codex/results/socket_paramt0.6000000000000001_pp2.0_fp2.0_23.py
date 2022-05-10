import socket
socket.if_indextoname(3)

# Open a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect to a host
s.connect(('www.python.org', 80))

# Get the local socket address
s.getsockname()

# Get the remote socket address
s.getpeername()

# Set socket options
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Get socket options
s.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)

# Send and receive data
s.send(b'GET / HTTP/1.0\r\nHost: www.python.org\r\n\r\n')
s.recv(8192)

# Send and receive data with buffering
s.sendall(b'GET / HTTP/1.0\r\nHost: www.python.org\r\n\r\n')
s.recv(8192)

# Receive data with
