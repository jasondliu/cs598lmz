import socket
# Test socket.if_indextoname
import socket
import sys

if sys.platform != 'darwin':
    skip("if_indextoname only supported on OSX")

ifname = socket.if_indextoname(1)
if ifname != 'lo0':
    print("if_indextoname(1) expected 'lo0', got '%s'" % ifname)
