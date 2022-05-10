import socket
socket.if_indextoname(3)

#if_nameindex()
socket.if_nameindex()

#if_nametoindex()
socket.if_nametoindex('lo')

#inet_aton()
socket.inet_aton('127.0.0.1')

#inet_ntoa()
socket.inet_ntoa(b'\x7f\x00\x00\x01')

#gethostname()
socket.gethostname()

#gethostbyname()
socket.gethostbyname('localhost')

#gethostbyname_ex()
socket.gethostbyname_ex('localhost')

#gethostbyaddr()
socket.gethostbyaddr('127.0.0.1')

#getfqdn()
socket.getfqdn('127.0.0.1')

#getaddrinfo()
socket.getaddrinfo('www.baidu.com',80)

#getnameinfo()
socket.getnameinfo(('www.baidu.com',80),0)

#getdefaulttimeout()
socket.
