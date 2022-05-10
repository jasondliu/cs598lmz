import socket
# Test socket.if_indextoname()
print "if_indextoname('0') = %s" % socket.if_indextoname(0)

import socket
# Test socket.close()
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.close()

import socket
# Test socket.socketpair()
server_socket, client_socket = socket.socketpair()
print "Server socket = %s" % server_socket
print "Client socket = %s" % client_socket

import socket
# Test socket.socketpair()
server_socket, client_socket = socket.socketpair()
# Note that this sequence of calls works in Python 2.3
client_socket.setblocking(1)
server_socket.setblocking(1)
# Python 2.4 socket objects have a recv() method.
server_socket.recv(1)
client_socket.send(".")

import socket
# Test socket.getcodebyname()
try:
  print socket.getaddrinfo('www.python.org', 80, family=2)
except socket
