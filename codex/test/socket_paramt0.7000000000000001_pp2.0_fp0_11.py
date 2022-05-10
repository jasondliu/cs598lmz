import socket
socket.if_indextoname(1)

socket.if_nameindex()

socket.if_nametoindex('en0')

socket.gethostbyname('python.org')

socket.gethostbyname_ex('python.org')

socket.gethostname()

socket.gethostbyaddr('192.168.0.1')

socket.getprotobyname('tcp')

socket.getservbyname('http')

socket.getaddrinfo('www.python.org', 'http')

socket.getaddrinfo('192.168.0.1', 80, socket.AF_INET, socket.SOCK_STREAM, 0, socket.AI_PASSIVE)

socket.getnameinfo(('www.python.org', 80), 0)

socket.getfqdn('192.168.0.1')

socket.getdefaulttimeout()

socket.setdefaulttimeout(30)

socket.getdefaulttimeout()

socket.AF_INET

socket.AF_INET6

socket.AF_UNIX

socket.AF_UNSPEC
