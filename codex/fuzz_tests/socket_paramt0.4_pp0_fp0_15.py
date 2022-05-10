import socket
socket.if_indextoname(2)

socket.if_nametoindex('eth0')

socket.gethostbyaddr('127.0.0.1')

socket.gethostbyname('localhost')

socket.gethostbyname_ex('localhost')

socket.gethostname()

socket.getnameinfo(('127.0.0.1', 80), 0)

socket.getprotobyname('tcp')

socket.getservbyname('http', 'tcp')

socket.getservbyport(80, 'tcp')

socket.getaddrinfo('www.python.org', 'http')

socket.getaddrinfo('www.python.org', 80, 0, 0, socket.IPPROTO_TCP)

socket.getaddrinfo('127.0.0.1', 0, socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP, socket.AI_PASSIVE)

socket.getaddrinfo('::1', 0, socket.AF_INET6, socket.SOCK_STREAM, 0, socket
