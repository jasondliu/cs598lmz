import socket
socket.if_indextoname(3)

socket.if_nameindex()

socket.if_nametoindex('en0')

socket.getaddrinfo('www.python.org', 'http')

socket.gethostbyname('www.python.org')

socket.gethostbyname_ex('www.python.org')

socket.gethostname()

socket.gethostbyaddr('192.168.0.1')

socket.getprotobyname('tcp')

socket.getservbyname('http', 'tcp')

socket.getnameinfo(('www.python.org', 80), 0)

socket.getnameinfo(('192.168.0.1', 80), 0)

socket.getsockopt(sock, socket.SOL_SOCKET, socket.SO_KEEPALIVE)

socket.setsockopt(sock, socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)

socket.socketpair()

socket.ntohs(0x1234)

socket.ntohl(0x
