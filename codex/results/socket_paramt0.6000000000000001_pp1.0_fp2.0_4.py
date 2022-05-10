import socket
socket.if_indextoname(3)

import socket
socket.if_nameindex()

import socket
socket.if_nametoindex('lo')

import socket
socket.gethostbyaddr('127.0.0.1')

import socket
socket.gethostbyname('localhost')

import socket
socket.gethostbyname_ex('localhost')

import socket
socket.gethostname()

import socket
socket.getnameinfo(('127.0.0.1', 80), 0)

import socket
socket.getprotobyname('tcp')

import socket
socket.getservbyname('http', 'tcp')

import socket
socket.getservbyport(80, 'tcp')

import socket
socket.getaddrinfo('www.python.org', 'http')

import socket
socket.getaddrinfo('127.0.0.1', 80, socket.AF_INET)

import socket
socket.getaddrinfo('127.0.0.1', 80, socket.AF_INET, socket.SOCK_STREAM)

import socket

