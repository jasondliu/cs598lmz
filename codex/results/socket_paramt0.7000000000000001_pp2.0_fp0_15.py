import socket
socket.if_indextoname(0)

import socket
socket.if_indextoname(1)

import socket
socket.if_indextoname(2)

# if_nameindex()

# if_freenameindex()

import socket
socket.getaddrinfo('www.google.com', 'http')

import socket
socket.getaddrinfo('www.google.com', 'http', type=socket.SOCK_STREAM)

import socket
socket.getaddrinfo('www.google.com', 'http', socket.AF_INET, socket.SOCK_STREAM)

import socket
socket.getaddrinfo('www.google.com', 'http', 0, socket.SOCK_STREAM, socket.SOL_TCP)

import socket
socket.getaddrinfo('www.google.com', 'http', 0, socket.SOCK_STREAM, socket.SOL_TCP, socket.AI_CANONNAME)

import socket
socket.getaddrinfo('www.google.com', 'http', 0, socket.SOCK_STREAM, socket.SOL
