import socket
# Test socket.if_indextoname()
# This returns the network interface name (eg 'eth0') corresponding to
# a given interface index.  If a name or index is not found, an exception
# is raised.
print 'lo :', socket.if_indextoname(1)
print 'eth0 :', socket.if_indextoname(2)
#print socket.if_indextoname(99)
#print socket.if_indextoname('eth1')

print '\n'

# Test socket.if_nameindex()
# This returns a list of tuples containing interface indices and names.
for i in socket.if_nameindex():
    print i[0], ':', i[1]

print '\n'

# Test socket.if_nametoindex()
# This returns the interface index corresponding to a given interface name,
# or raises an exception if the name or index is not found.
print '1 :', socket.if_nametoindex('lo')
print '2 :', socket.if_nametoindex('eth0')
#print socket.if_nametoindex('
