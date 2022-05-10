import socket
socket.if_indextoname(7)

# Module
import socket
socket.getaddrinfo('www.google.com', 80, 0, 0, socket.IPPROTO_TCP)

import socket
socket.getaddrinfo('www.google.com', 80, 0, 0, socket.IPPROTO_IP)

import socket
socket.getaddrinfo('www.google.com', 80, 0, 0, socket.IPPROTO_IP, socket.SOCK_DGRAM)

import socket
socket.getaddrinfo('www.google.com', 80, socket.AF_UNSPEC, 0, socket.IPPROTO_IP, socket.SOCK_DGRAM)


# Module
import socket
socket.getaddrinfo('www.google.com', 'http')

# Module
import socket
socket.getaddrinfo('www.google.com', 'http', 0, 0, 0, socket.AI_ADDRCONFIG | socket.AI_V4MAPPED | socket.AI_CANONNAME)

# Module
import socket
socket.getaddrinfo('ipv6.google.com', '
