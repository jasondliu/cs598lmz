import socket
socket.if_indextoname("i")

# ---------------------------------------------------------------------

# 2.2.2
# Import the socket library and create a new socket
import socket
s = socket.socket()

# ---------------------------------------------------------------------

# 2.2.3
# Import the socket library and create a new socket
import socket
s = socket.socket()

# Bind the socket to the port
s.bind(("localhost", 12345))

# Listen for connections
s.listen(5)

# ---------------------------------------------------------------------

# 2.2.4
# Import the socket library and create a new socket
import socket
s = socket.socket()

# Bind the socket to the port
s.bind(("localhost", 12345))

# Listen for connections
s.listen(5)

# Accept connections
c_socket, address = s.accept()

# ---------------------------------------------------------------------

# 2.2.5
# Import the socket library and create a new socket
import socket
s = socket.socket()

# Bind the socket to the port
s.bind(("localhost", 12345))

# Listen for connections
s.listen(5
