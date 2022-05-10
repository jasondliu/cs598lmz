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
print socket.if_indextoname(ifindex)
from test.test_socket import if_indextoname
print if_indextoname(ifindex)
from socket import if_indextoname
print if_indextoname(ifindex)
print socket.if_indextoname(0)
for ifindex in range(10):
    ifname = socket.if_indextoname(ifindex)
    print ifname,
print
print socket.if_nametoindex('lo')
from socket import if_nametoindex
print if_nametoindex('lo')
print if_nametoindex('loopback')
print if_nametoindex('not a name')
if socket.has_ipv6:
    print socket.
