import socket
# Test socket.if_indextoname
print(socket.if_indextoname(1))
# Test socket.if_nameindex
print(socket.if_nameindex())
# Test socket.socketpair
print(socket.socketpair())
# Test socket.getaddrinfo
print(socket.getaddrinfo("www.python.org", "http", 0, socket.SOCK_STREAM))
# Test socket.getnameinfo
print(socket.getnameinfo(('127.0.0.1', 8080), 0))
# Test socket.getfqdn
print(socket.getfqdn("8.8.8.8"))
# Test socket.gethostbyname
print(socket.gethostbyname("www.python.org"))
# Test socket.gethostbyname_ex
print(socket.gethostbyname_ex("www.python.org"))
# Test socket.gethostname
print(socket.gethostname())
# Test socket.gethostbyaddr
print(socket.gethostbyaddr("127.0.0.1"))
# Test socket.getprotobyname
print(socket.
