import socket
socket.if_indextoname(1)

socket.if_nameindex()

socket.if_nametoindex('en0')

socket.gethostbyname('hostname')

socket.gethostbyname_ex('hostname')

socket.gethostbyaddr('127.0.0.1')

socket.getnameinfo(('127.0.0.1', 80), 0)

socket.getaddrinfo('www.python.org', 'http')

# added in python 3.3
socket.getaddrinfo('www.python.org', 'http', 0, socket.SOCK_STREAM, 0, socket.AI_ADDRCONFIG | socket.AI_V4MAPPED)

socket.getfqdn('127.0.0.1')

socket.gethostbyname_ex('localhost')

# added in python 3.3
socket.gethostbyname_ex('localhost', 0, 0)

socket.gethostbyname_ex('localhost', 0, socket.AI_ADDRCONFIG)
