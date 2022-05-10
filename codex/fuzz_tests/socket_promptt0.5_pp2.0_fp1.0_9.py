import socket
# Test socket.if_indextoname and socket.if_nameindex

print "Testing if_indextoname()"
try:
    socket.if_indextoname(1)
except socket.error, msg:
    print "if_indextoname() failed:", msg
else:
    print "if_indextoname() succeeded"

print "Testing if_nameindex()"
try:
    socket.if_nameindex()
except socket.error, msg:
    print "if_nameindex() failed:", msg
else:
    print "if_nameindex() succeeded"
