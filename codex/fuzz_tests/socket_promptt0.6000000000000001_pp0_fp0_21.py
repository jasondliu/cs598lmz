import socket
# Test socket.if_indextoname()

print "Test IPv4"
for i in range(2,9):
    print "if_indextoname(%d) = %s" % (i, socket.if_indextoname(i))

print "Test IPv6"
for i in range(10,12):
    print "if_indextoname(%d) = %s" % (i, socket.if_indextoname(i))

print "Test invalid index"
try:
    socket.if_indextoname(1)
except socket.error, e:
    print "socket.error:", e
else:
    print "socket.if_indextoname(1) must raise a socket.error"
