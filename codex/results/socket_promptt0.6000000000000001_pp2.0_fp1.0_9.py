import socket
# Test socket.if_indextoname()

# This test requires an interface with an IPv6 address configured
# (or an IPv6-capable interface on Windows).

import socket
import sys

if sys.platform == 'win32':
    # On Windows, if_indextoname() takes an integer, not a string.
    def if_indextoname(i):
        return socket.if_indextoname(int(i))
else:
    if_indextoname = socket.if_indextoname

if socket.has_ipv6:
    for i in socket.if_nameindex():
        name = i[1]
        try:
            print(name, if_indextoname(name))
        except socket.error:
            pass
