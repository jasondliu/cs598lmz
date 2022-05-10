import socket
# Test socket.if_indextoname()
import errno
from test import support
import array
import sys

if hasattr(socket, 'if_indextoname'):
    interface_name = socket.if_indextoname(2)
    interface_index = socket.if_nametoindex(interface_name)
    if interface_index != 2:
        print('socket.if_indextoname() and socket.if_nametoindex()',
              'are inconsistent')
        print('socket.if_indextoname(2) is %r' % interface_name)
        print('socket.if_nametoindex(%r) is %r' % (interface_name,
              interface_index))
    if not isinstance(interface_name, str):
        print('socket.if_indextoname() did not return a string')
        print('it returned %r' % type(interface_name))
    if not isinstance(interface_index, int):
        print('socket.if_nametoindex() did not return an int')
        print('it returned %r' % type(interface_index
