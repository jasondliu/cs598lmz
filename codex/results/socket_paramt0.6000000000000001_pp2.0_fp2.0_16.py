import socket
socket.if_indextoname(2)

# Get the name of the interface with the given index
socket.if_nameindex()

# Get the index of the interface with the given name
socket.if_nametoindex('eth0')

# Get socket information
socket.getsockopt(s, socket.SOL_SOCKET, socket.SO_REUSEADDR)

# Set socket information
socket.setsockopt(s, socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Get socket name
socket.getsockname(s)

# Get socket peer name
socket.getpeername(s)

# Get socket error
socket.geterror()

# Create a socket pair
socket.socketpair()

# Get the default timeout value
socket.getdefaulttimeout()

# Set the default timeout value
socket.setdefaulttimeout(10)

# Create a new socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to a remote socket
s.connect(("www.python.org", 80))
