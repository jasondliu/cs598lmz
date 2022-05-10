import socket
# Test socket.if_indextoname()
for name in socket.if_nameindex():
    print "%s %s" % name, socket.if_indextoname(name[0])

print "==="
# Test socket.if_indextoname() w/o arguments
print socket.if_indextoname()

print "==="
# Test socket.if_indextoname() error detection
try:
    print socket.if_indextoname(-1)
except ValueError:
    print "Test passed!"
except Exception, e:
    print "Test failed! Unexpected exception: %s" % e

print "==="
# Test socket.if_nameindex()
for name in socket.if_nameindex():
    print "%s %s" % name, socket.if_indextoname(name[0])

print "==="
# Test socket.if_nameindex() w/o arguments
print socket.if_nameindex()

print "==="
# Test socket.if_nameindex() error detection
try:
    print socket.if_nameindex(-1)
except
