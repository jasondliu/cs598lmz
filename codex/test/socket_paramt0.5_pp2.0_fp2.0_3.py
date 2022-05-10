import socket
socket.if_indextoname(0x1)

# Get the socket name
s.getsockname()

# Get the peer name
s.getpeername()

# Send data to the server
s.send(b'Hi there, server')

# Receive data from the server
s.recv(1024)

# Close the connection
