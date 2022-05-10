import socket
socket.if_indextoname(3)

# Create a new socket using the given address family, socket type and protocol number
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Return the current address family of the socket
s.family

# Return the current socket type
s.type

# Return the current protocol number
s.proto

# Return the socket’s file descriptor
s.fileno()

# Return the socket’s timeout
s.gettimeout()

# Return the address of the remote endpoint
s.getpeername()

# Return the address of the local endpoint
s.getsockname()

# Return the value of the given socket option
s.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)

# Return the socket’s timeout
s.gettimeout()

# Return True if the socket is closed, False otherwise
s.closed

# Return True if the socket is listening, False otherwise
s.listening

# Return True if the socket is connected, False otherwise
s.connected


