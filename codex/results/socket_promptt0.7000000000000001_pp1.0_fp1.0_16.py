import socket
# Test socket.if_indextoname
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print(socket.if_indextoname(s.getsockopt(socket.SOL_SOCKET, socket.SO_IFINDEX)))

# Test socket.SO_NOSIGPIPE
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_NOSIGPIPE, 1)
print("ok")
