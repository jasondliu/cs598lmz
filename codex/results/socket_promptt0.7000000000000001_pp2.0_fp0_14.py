import socket
# Test socket.if_indextoname() function
import socket
if socket.has_ipv6:
    print 'Socket has IPv6'
    index = socket.if_nametoindex('lo')
    name = socket.if_indextoname(index)
    print 'lo index is %d , name is %s' % (index, name)
else:
    print 'Socket does not have IPv6'

# Test socket.has_ipv6 function
