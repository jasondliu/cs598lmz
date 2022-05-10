import socket
# Test socket.if_indextoname() in IPv6 mode

import support

try:
    socket.if_indextoname(1)
except socket.error:
    pass
