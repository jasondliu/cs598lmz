import socket
# Test socket.if_indextoname()
print(socket.if_indextoname(0))
# Test socket.if_nameindex()
print(socket.if_nameindex())
# Test socket.if_nametoindex()
print(socket.if_nametoindex('lo'))
# Test socket.if_nametoindex() with invalid interface
try:
    print(socket.if_nametoindex('enp3s0'))
except Exception as e:
    print(e)

# Test socket.getaddrinfo()
print(socket.getaddrinfo('localhost', 80))
# Test socket.gethostbyname()
print(socket.gethostbyname('localhost'))
# Test socket.gethostbyname_ex()
print(socket.gethostbyname_ex('localhost'))
# Test socket.gethostname()
print(socket.gethostname())
# Test socket.getnameinfo()
print(socket.getnameinfo(('localhost', 80), 0))
# Test socket.getprotobyname()
print(socket.getprotobyname('tcp'))
# Test socket.
