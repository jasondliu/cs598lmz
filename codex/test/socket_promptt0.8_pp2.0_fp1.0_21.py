import socket
# Test socket.if_indextoname()


import socket
import sys
import subprocess

addresses = [
    ('127.0.0.1', 0),
    ('localhost', 0),
    ('::1', 0),
    ('::ffff:127.0.0.1', 0),
    ('::ffff:7f00:1', 0),
    ('fe80::ffff:127.0.0.1%lo0', 0),
    ('fe80::ffff:7f00:1%lo0', 0),
    ('fe80::1%lo0', 0),
    ('fe80::', 0),
]

for (host, port) in addresses:
    print('{:24} :'.format(host), end=' ')
    try:
        index = socket.if_nametoindex(host)
    except OSError as msg:
        print('if_nametoindex() failed:', msg)
        continue
    index2 = socket.if_nametoindex('lo0')
    name = socket.if_indextoname(index)
