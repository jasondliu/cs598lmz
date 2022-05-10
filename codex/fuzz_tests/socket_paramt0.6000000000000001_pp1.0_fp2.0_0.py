import socket
socket.if_indextoname(5)

print("---")

import socket
socket.if_nameindex()

print("---")

import socket
socket.if_nametoindex('lo0')

print("---")

import socket
socket.inet_aton('192.168.0.1')

print("---")

import socket
socket.inet_ntoa(b'\xc0\xa8\x00\x01')

print("---")

import socket
socket.getaddrinfo('www.python.org', 'http', 0, 0, socket.IPPROTO_TCP)

print("---")

import socket
socket.getaddrinfo('www.python.org', 'http', 0, 0, socket.IPPROTO_TCP, socket.AI_CANONNAME)

print("---")

import socket
socket.getaddrinfo('www.python.org', 'http', 0, 0, socket.IPPROTO_TCP, socket.AI_CANONNAME, socket.AI_PASSIVE)

print("---")

import socket
socket.getaddr
