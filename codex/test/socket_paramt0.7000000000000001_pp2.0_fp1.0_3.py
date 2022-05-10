import socket
socket.if_indextoname(2)
socket.if_nametoindex('en0')
socket.if_nameindex()
socket.if_nameindex()[0][1]
[(i, j) for i, j in socket.if_nameindex()]
for i, j in socket.if_nameindex():
    print(i, j)
socket.getaddrinfo('www.python.org', 'http')
socket.getaddrinfo('www.python.org', 'http', 0, socket.SOCK_STREAM, 0, socket.AI_PASSIVE)
socket.getaddrinfo('www.python.org', 'http', 0, socket.SOCK_STREAM, 0, socket.AI_PASSIVE | socket.AI_CANONNAME)
socket.getaddrinfo('www.python.org', 'http', 0, socket.SOCK_STREAM, 0, socket.AI_PASSIVE | socket.AI_CANONNAME)
