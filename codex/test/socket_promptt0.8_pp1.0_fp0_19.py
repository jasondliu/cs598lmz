import socket
# Test socket.if_indextoname()'s existence
try:
    socket.if_indextoname
except AttributeError:
    print("SKIP")
    raise SystemExit

# Create a socket with no filter
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)

# Get the interface indices
idx1 = sock.getsockopt(socket.SOL_SOCKET, socket.SO_BINDTODEVICE, b'eth0')
idx2 = sock.getsockopt(socket.SOL_SOCKET, socket.SO_BINDTODEVICE, b'lo')

# Check the names
try:
    print(socket.if_indextoname(idx1))
except OSError:
    print("unknown")
try:
    print(socket.if_indextoname(idx2))
except OSError:
    print("unknown")
