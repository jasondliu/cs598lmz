import socket
socket.if_indextoname(3)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('', 0))
s.getsockname()[4][0]

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('8.8.8.8', 80))
s.getsockname()[0]

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('8.8.8.8', 80))
s.getsockname()[0]

import socket
socket.gethostbyname('localhost')

import socket
socket.gethostbyname('localhost')

import socket
socket.gethostbyname('localhost')

import socket
socket.gethostbyname('localhost')

import socket
socket.gethostbyname('localhost')

import socket
socket.gethostbyname('localhost')

import socket
socket.gethostbyname('localhost')

import socket
socket.gethostby
