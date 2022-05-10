import socket
socket.if_indextoname(3)

socket.if_nametoindex('lo')

socket.gethostbyaddr('127.0.0.1')

socket.gethostbyname('localhost')

socket.gethostbyname_ex('localhost')

socket.gethostname()

socket.getfqdn()

socket.gethostbyname_ex(socket.gethostname())

socket.gethostbyname_ex(socket.getfqdn())

socket.getaddrinfo('www.python.org', 'http')

socket.getaddrinfo('www.python.org', 80, socket.AF_INET, socket.SOCK_STREAM)

socket.getaddrinfo('www.python.org', 80, socket.AF_INET, socket.SOCK_STREAM, 0, socket.AI_ADDRCONFIG)

socket.getaddrinfo('127.0.0.1', 80, socket.AF_INET, socket.SOCK_STREAM)

