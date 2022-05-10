import socket
# Test socket.if_indextoname
socket.if_indextoname(1)

# Test socket.if_nameindex
socket.if_nameindex()

# Test socket.if_nametoindex
socket.if_nametoindex('lo0')

# Test socket.socket
s = socket.socket()

# Test socket.socketpair
s1, s2 = socket.socketpair()

# Test socket.getaddrinfo
socket.getaddrinfo('127.0.0.1', 23, socket.AF_INET, socket.SOCK_STREAM)

# Test socket.getnameinfo
socket.getnameinfo(('127.0.0.1', 23), 0)

# Test socket.getfqdn
socket.getfqdn('127.0.0.1')

# Test socket.gethostbyaddr
socket.gethostbyaddr('127.0.0.1')

# Test socket.gethostbyname
socket.gethostbyname('localhost')

# Test socket.gethostbyname_ex
socket.gethostbyname_ex('localhost')


