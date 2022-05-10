import socket
socket.if_indextoname(1)

#if_nameindex()
socket.if_nameindex()

#if_nametoindex()
socket.if_nametoindex('eth0')

#gethostbyaddr()
socket.gethostbyaddr('127.0.0.1')

#gethostbyname()
socket.gethostbyname('localhost')

#gethostbyname_ex()
socket.gethostbyname_ex('localhost')

#gethostname()
socket.gethostname()

#getnameinfo()
socket.getnameinfo(('127.0.0.1', 80), 0)

#getprotobyname()
socket.getprotobyname('tcp')

#getservbyname()
socket.getservbyname('http', 'tcp')

#getservbyport()
socket.getservbyport(80, 'tcp')

#getaddrinfo()
socket.getaddrinfo('www.python.org', 'http')

#getdefaulttimeout()
socket.getdefaulttimeout()

#setdefaulttimeout()
socket
