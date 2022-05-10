import socket
# Test socket.if_indextoname using a numeric index.
import socket
import sys
import test_support

if hasattr(socket, 'if_indextoname'):
    try:
        socket.if_indextoname(0)
    except socket.error:
        pass
    else:
        print 'socket.if_indextoname(0) should have raised socket.error'
        sys.exit(1)
    ifname = socket.if_indextoname(1)
    if ifname is None:
        print 'socket.if_indextoname(1) returned None'
        sys.exit(1)
    print 'socket.if_indextoname(1) returned %r' % ifname
    index = socket.if_nametoindex(ifname)
    if index != 1:
        print 'socket.if_nametoindex(%r) returned %d instead of 1' % (ifname, index)
        sys.exit(1)
    print 'socket.if_nametoindex(%r) returned %d' % (ifname, index)
    # If
