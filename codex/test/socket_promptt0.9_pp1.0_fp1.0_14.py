import socket
# Test socket.if_indextoname
from test_support import import_module
import_module('socket')
hostname = 'www.w3.org'
hostip = socket.gethostbyname(hostname)
ifindex = 0
while not hostip:
    ifindex += 1
    hostip = socket.gethostbyname(hostname, ifindex)
