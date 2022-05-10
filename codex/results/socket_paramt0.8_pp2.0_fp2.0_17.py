import socket
socket.if_indextoname(2)
'en0'
socket.if_indextoname(3)
'pdp_ip0'
socket.if_indextoname(4)
'awdl0'

import socket
socket.getaddrinfo('0.0.0.0', 80)
[(2, 2, 0, '', ('0.0.0.0', 80)),
 (2, 1, 6, '', ('0.0.0.0', 80)),
 (30, 2, 0, '', ('0.0.0.0', 80)),
 (30, 1, 6, '', ('0.0.0.0', 80)),
 (23, 2, 0, '', ('0.0.0.0', 80)),
 (23, 1, 6, '', ('0.0.0.0', 80)),
 (24, 2, 0, '', ('0.0.0.0', 80))]

import socket
socket.getnameinfo(('127.0.0.1', 80), 0)
('localhost', 'http')

from socket import ntohl

