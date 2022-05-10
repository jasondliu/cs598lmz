import socket
socket.if_indextoname(1)

# Get the IP address of the interface.
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
