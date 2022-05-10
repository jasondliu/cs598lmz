import socket
socket.if_indextoname(3)

import socket
socket.gethostname()

import socket
socket.gethostbyname('www.python.org')

import socket
socket.gethostbyname_ex('www.python.org')

import socket
socket.gethostbyaddr('216.34.181.96')

import socket
socket.getservbyname('http')

import socket
socket.getservbyport(80)

import socket
socket.getaddrinfo('www.python.org', 'http')

import socket
socket.getaddrinfo('www.python.org', 80, socket.AF_INET, socket.SOCK_STREAM)

import socket
socket.getaddrinfo('www.python.org', 80, socket.AF_INET, socket.SOCK_STREAM, socket.SOL_TCP)

import socket
socket.getaddrinfo('www.python.org', 80, socket.AF_INET, socket.SOCK_STREAM, 0, socket.AI_ADDRCONFIG)

import socket
socket.getaddrinfo('www.python.
