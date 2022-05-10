import socket
# Test socket.if_indextoname()
print "if_indextoname():"
for i in range(1, 10):
    try:
        print "\tinterface index %d: %s" % (i, socket.if_indextoname(i))
    except Exception, e:
        print "\tinterface index %d: %s" % (i, e)

# Test socket.if_indextoname()
print "if_indextoname():"
for i in range(1, 10):
    try:
        print "\tinterface index %d: %s" % (i, socket.if_indextoname(i))
    except:
        print "\tfailed to get info for interface index %d" % (i)

# Test socket.if_nametoindex()
print "if_nametoindex():"
for i in range(1, 10):
    try:
        print "\tinterface name lo: %d" % socket.if_nametoindex('lo')
        print "\tinterface name eth0: %d" % socket.if_nametoindex('eth0')
       
