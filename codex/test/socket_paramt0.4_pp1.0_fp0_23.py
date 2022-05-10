import socket
socket.if_indextoname(1)

import socket
socket.if_nameindex()

import socket
socket.if_nametoindex('lo')

import socket
socket.getaddrinfo('localhost', None)

import socket
socket.getaddrinfo('localhost', None, socket.AF_INET)

import socket
socket.getaddrinfo('localhost', None, socket.AF_INET, socket.SOCK_STREAM)

import socket
socket.getaddrinfo('localhost', None, socket.AF_INET, socket.SOCK_STREAM, 0, socket.AI_PASSIVE)

import socket
socket.getaddrinfo('localhost', None, socket.AF_INET, socket.SOCK_STREAM, 0, socket.AI_PASSIVE, socket.AI_CANONNAME)

import socket
socket.getaddrinfo('localhost', None, socket.AF_INET, socket.SOCK_STREAM, 0, socket.AI_PASSIVE, socket.AI_CANONNAME, socket.AI_NUMERICHOST)

import socket
