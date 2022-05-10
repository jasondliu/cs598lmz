import socket
# Test socket.if_indextoname
socket.if_indextoname(1)

# Test socket.if_nametoindex
socket.if_nametoindex('lo')

# Test socket.gethostbyaddr
socket.gethostbyaddr('127.0.0.1')
socket.gethostbyaddr('localhost')

# Test socket.gethostbyname
socket.gethostbyname('localhost')
