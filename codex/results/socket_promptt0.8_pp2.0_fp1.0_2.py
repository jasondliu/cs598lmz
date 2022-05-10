import socket
# Test socket.if_indextoname()

try:
    socket.if_indextoname(2)
    print 'if_indextoname passed'
except:
    print 'if_indextoname failed'

# Test socket.if_nametoindex()

try:
    socket.if_nametoindex('lo')
    print 'if_nametoindex passed'
except:
    print 'if_nametoindex failed'

# Test socket.getifaddrs()

try:
    socket.getifaddrs()
    print 'getifaddrs passed'
except:
    print 'getifaddrs failed'

# Test socket.if_nameindex()

try:
    socket.if_nameindex()
    print 'if_nameindex passed'
except:
    print 'if_nameindex failed'
