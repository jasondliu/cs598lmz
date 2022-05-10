import socket
# Test socket.if_indextoname()

import socket
import sys

if sys.platform == 'win32':
    print('Windows')
    print(socket.if_indextoname(1))
else:
    print('Linux')
    print(socket.if_indextoname(2))

# Test socket.if_nameindex()

import socket
import sys

if sys.platform == 'win32':
    print('Windows')
    print(socket.if_nameindex())
else:
    print('Linux')
    print(socket.if_nameindex())

# Test socket.if_nametoindex()

import socket
import sys

if sys.platform == 'win32':
    print('Windows')
    print(socket.if_nametoindex('Loopback Pseudo-Interface 1'))
else:
    print('Linux')
    print(socket.if_nametoindex('lo'))

# Test socket.getaddrinfo()

import socket
import sys

if sys.platform == 'win32':
    print('Windows')
