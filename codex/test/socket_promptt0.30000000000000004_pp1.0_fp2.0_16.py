import socket
# Test socket.if_indextoname()

import socket
import sys
import os

if sys.platform == 'win32':
    print('Windows does not support this test')
    sys.exit(0)

if_name = 'lo'
if_index = socket.if_nametoindex(if_name)
if_index_name = socket.if_indextoname(if_index)

if if_index_name != if_name:
    print('Error: if_indextoname() returned %s, expected %s' % (if_index_name, if_name))
    sys.exit(1)

print('if_indextoname() returned %s, expected %s' % (if_index_name, if_name))

# Test socket.if_nameindex()
if_name_index = socket.if_nameindex()
if_name_index_dict = dict(if_name_index)

if if_name not in if_name_index_dict:
    print('Error: if_nameindex() did not return %s' % if_name)
    sys
