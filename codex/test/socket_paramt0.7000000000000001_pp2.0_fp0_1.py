import socket
socket.if_indextoname(4)

# The next step is to get the interface's IP address:
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# This call requests the interface's current IP address.
