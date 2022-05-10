import socket
socket.if_indextoname(2)

import socket
socket.if_nameindex()

import socket
socket.if_nametoindex('lo')

import socket
socket.gethostbyname('www.python.org')

import socket
socket.gethostbyname_ex('www.python.org')

import socket
socket.gethostbyaddr('93.184.216.34')

import socket
socket.getnameinfo(('93.184.216.34', 80), socket.NI_NAMEREQD)

import socket
socket.getnameinfo(('93.184.216.34', 80), 0)

import socket
socket.getaddrinfo('www.python.org', 'http')

import socket
socket.getaddrinfo('www.python.org', 80, 0, 0, socket.IPPROTO_TCP)

import socket
socket.getaddrinfo('127.0.0.1', 8080)

import socket
socket.getaddrinfo('127.0.0.1', 8080, socket.AF_INET, socket.SOCK_STREAM, 0
