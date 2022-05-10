import socket
# Test socket.if_indextoname()
import socket
import sys

if sys.platform == 'darwin':
    # On OSX, if_indextoname() returns the interface name
    # as a string, not bytes.
    def if_indextoname(index):
        return socket.if_indextoname(index)
else:
    # On other platforms, if_indextoname() returns the interface name
    # as bytes.
    def if_indextoname(index):
        return socket.if_indextoname(index).encode('ascii')

# Test socket.if_nameindex()
import socket
import sys

if sys.platform == 'darwin':
    # On OSX, if_nameindex() returns the interface name
    # as a string, not bytes.
    def if_nameindex():
        return socket.if_nameindex()
