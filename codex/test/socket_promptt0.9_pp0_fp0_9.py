import socket
# Test socket.if_indextoname convert 100 to 'eth0'
Socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
Index = Socket.if_indextoname(100)
