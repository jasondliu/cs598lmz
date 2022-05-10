import socket
# Test socket.if_indextoname
s = socket.socket()

# Error conditions.
try:
    socket.if_indextoname(s, 'spam')
except TypeError:
    pass
else:
    print('TypeError expected')

try:
    socket.if_indextoname('spam', 'spam')
except TypeError:
    pass
else:
    print('TypeError expected')

try:
    socket.if_indextoname(-1, 2)
excep
