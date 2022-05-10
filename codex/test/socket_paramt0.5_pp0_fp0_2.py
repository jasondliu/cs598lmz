import socket
socket.if_indextoname(1)

import socket
socket.if_nameindex()

import socket
socket.gethostbyname('www.python.org')

import socket
socket.gethostbyname_ex('www.python.org')

import socket
socket.gethostbyaddr('93.184.216.34')

import socket
socket.getnameinfo('93.184.216.34', 0)

import socket
socket.getaddrinfo('www.python.org', 'http')

import socket
socket.getaddrinfo('www.python.org', 'http', 0, socket.SOCK_STREAM, 0, socket.AI_CANONNAME)

import socket
socket.getaddrinfo('www.python.org', 'http', 0, socket.SOCK_STREAM, 0, socket.AI_CANONNAME, socket.AI_ALL)

import socket
socket.getaddrinfo('www.python.org', 'http', 0, socket.SOCK_STREAM, 0, socket.AI_CANONNAME, socket.AI_ALL, None)

import socket
