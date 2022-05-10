import socket
socket.if_indextoname(12)

# The socket address is a tuple consisting of an IP address and a port number.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 50000))

s.listen(1)  # Listen for connections made to the socket.
# The argument to listen is the number of connections to accept before refusing new connections.

