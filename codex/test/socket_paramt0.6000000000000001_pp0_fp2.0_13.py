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
socket.gethostname()

import socket
socket.sethostname('hostname')

import socket
socket.gethostbyname_ex('localhost')

import socket
socket.gethostbyaddr('127.0.0.1')

import socket
socket.getnameinfo(('127.0.0.1', 80), 0)

import socket
socket.getnameinfo(('127.0.0.1', 80), socket.NI_NAMEREQD)

import socket
socket.getnameinfo(('127.0.0.1', 80), socket.NI_NUMERICHOST)

import socket
socket.getnameinfo(('127.0.0.1', 80), socket.NI_NUMERICSERV)

import socket
