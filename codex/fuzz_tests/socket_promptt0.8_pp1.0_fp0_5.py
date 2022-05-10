import socket
# Test socket.if_indextoname

from socket import if_indextoname
from socket import if_nameindex

print if_indextoname(0)
print if_indextoname(1)

try:
    if_indextoname(2)
except ValueError:
    print 'ValueError'

try:
    if_indextoname(-1)
except ValueError:
    print 'ValueError'
