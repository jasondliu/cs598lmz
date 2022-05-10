import socket
# Test socket.if_indextoname
print(socket.if_indextoname(1))

import socket
# Test socket.if_nameindex
print(socket.if_nameindex())

import socket
# Test socket.if_nametoindex
print(socket.if_nametoindex('tap0'))

import socket
# Test socket.getservbyname
print(socket.getservbyname('ftp', 'tcp'))

import socket
# Test socket.getservbyport
print(socket.getservbyport(80, 'tcp'))

import socket
# Test socket.getprotobyname
print(socket.getprotobyname('tcp'))

import socket
# Test socket.getprotobynumber
print(socket.getprotobynumber(6))

import socket
# Test socket.th_off
print(socket.th_off)

import socket
# Test socket.tcpi_rcv_ssthresh_default
print(socket.tcpi_rcv_ssthresh_default)

import socket
# Test socket.tcpi
