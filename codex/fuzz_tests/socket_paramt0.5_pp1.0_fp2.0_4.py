import socket
socket.if_indextoname(2)

socket.if_nametoindex('en1')

socket.if_nameindex()

socket.if_nameindex()[1][1]

socket.gethostbyname('www.python.org')

socket.gethostbyname_ex('www.python.org')

socket.gethostname()

socket.gethostbyaddr('127.0.0.1')

socket.getprotobyname('tcp')

socket.getservbyname('http')

socket.getservbyport(80, 'tcp')

socket.getaddrinfo('www.python.org', 'http')

socket.getaddrinfo('127.0.0.1', 8080, socket.AF_INET, socket.SOCK_STREAM)

socket.getaddrinfo('127.0.0.1', 8080, 0, socket.SOCK_STREAM)

socket.getaddrinfo('127.0.0.1', 8080, socket.AF_UNSPEC, 0, socket.IPPROTO_TCP)

socket.
