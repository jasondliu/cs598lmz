import socket
socket.if_indextoname(1)

import socket
socket.if_nametoindex('lo')



import socket
socket.gethostbyname('localhost')

import socket
socket.gethostbyname_ex('localhost')

import socket
socket.gethostbyaddr('127.0.0.1')

import socket
socket.getnameinfo(('127.0.0.1', 80), 0)


import socket
socket.getaddrinfo("www.python.org", 80)


import socket
socket.getaddrinfo("www.python.org", 80, 0, 0, socket.IPPROTO_TCP)



import socket
socket.getaddrinfo("www.python.org", None)



import socket
socket.getaddrinfo("127.0.0.1", 80, socket.AF_INET, socket.SOCK_STREAM)



import socket
socket.gethostbyname_ex('www.python.org')

import socket
socket.gethostbyname_ex('www.python.org')[2]


import socket
socket.gethostbyname
