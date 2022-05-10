import socket
# Test socket.if_indextoname
if socket.if_indextoname(1):
    pass
# Test socket.if_nametoindex
if socket.if_nametoindex('test'):
    pass
# Test socket.if_nameindex
if socket.if_nameindex():
    pass

# Test socket.socketpair
socket.socketpair()

# Test socket.getaddrinfo and socket.getnameinfo
socket.getaddrinfo('localhost', 80)
socket.getaddrinfo('localhost', 80, 0, 0, socket.IPPROTO_TCP)
socket.getnameinfo(('127.0.0.1', 80), 0)


# Test socket.gethostbyname and socket.gethostbyname_ex
socket.gethostbyname('localhost')
socket.gethostbyname_ex('localhost')

# Test socket.gethostbyaddr
socket.gethostbyaddr('127.0.0.1')

# Test socket.gethostname
socket.gethostname()

# Test socket.gethostbyname_ex
socket.gethostbyname_ex('localhost')

