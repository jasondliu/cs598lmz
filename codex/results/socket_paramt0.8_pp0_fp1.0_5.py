import socket
socket.if_indextoname('46')

import ctypes

libc = ctypes.CDLL('libc.dylib')
libc.if_indextoname('46')

libc.if_indextoname(46)

import ctypes
ctypes.cdll.LoadLibrary('libSystem.dylib')

import socket
if socket.has_ipv6:
    print "socket.has_ipv6 is true"

socket.has_ipv6

socket.AF_INET6

socket.getaddrinfo('google.com', 80, socket.AF_INET6)

socket.getaddrinfo('google.com', 80, socket.AF_INET)

socket.getaddrinfo('google.com', 80)

socket.getaddrinfo('google.com', 80, socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_IP)

s = socket.socket()
s.bind(('0.0.0.0', 8080))
s.listen(5)
s.accept()


s = socket.
