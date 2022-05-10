import socket
socket.if_indextoname(2)

# --------------------------

import socket
socket.gethostbyaddr('127.0.0.1')

# --------------------------

import socket
socket.getfqdn('127.0.0.1')

# --------------------------

import socket
socket.gethostbyname('localhost')

# --------------------------

import socket
socket.gethostbyname_ex('localhost')

# --------------------------

import socket
socket.gethostname()

# --------------------------

import socket
socket.gethostbyname_ex(socket.gethostname())

# --------------------------

import socket
socket.getservbyname('ssh')

# --------------------------

import socket
socket.getservbyport(22)

# --------------------------

import socket
socket.getprotobyname('tcp')

# --------------------------

import socket
socket.fromfd(1, socket.AF_INET, socket.SOCK_STREAM)

# --------------------------

