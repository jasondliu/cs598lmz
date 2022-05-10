import socket
socket.if_indextoname(3)

#if_nameindex()
socket.if_nameindex()

#if_nametoindex()
socket.if_nametoindex('eth0')

#inet_aton()
socket.inet_aton('127.0.0.1')

#inet_ntoa()
socket.inet_ntoa(b'\x7f\x00\x00\x01')

#gethostbyaddr()
socket.gethostbyaddr('127.0.0.1')

#gethostbyname()
socket.gethostbyname('localhost')

#gethostbyname_ex()
socket.gethostbyname_ex('localhost')

#gethostname()
socket.gethostname()

#getprotobyname()
socket.getprotobyname('tcp')

#getservbyname()
socket.getservbyname('http')

#getservbyport()
socket.getservbyport(80)

#getaddrinfo()
socket.getaddrinfo('localhost', 80)

#getnameinfo()
socket
