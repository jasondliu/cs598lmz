import socket
# Test socket.if_indextoname(8)
socket.if_indextoname(8)
# Test socket.if_nameindex()
socket.if_nameindex()
# Test socket.if_nametoindex('lo')
socket.if_nametoindex('lo')
# Test socket.gethostname()
socket.gethostname()
# Test socket.gethostbyname(gethostname())
socket.gethostbyname(socket.gethostname())
# Test socket.gethostbyaddr(gethostbyname(gethostname()))
socket.gethostbyaddr(socket.gethostbyname(socket.gethostname()))
# Test socket.getfqdn(gethostname())
socket.getfqdn(socket.gethostname())
# Test socket.getaddrinfo(gethostname(), None)
socket.getaddrinfo(socket.gethostname(), None)
# Test socket.getaddrinfo('localhost', None)
socket.getaddrinfo('localhost', None)
# Test socket.getnameinfo(('127.0.0.1', 80), 0)
socket.getnameinfo(('
