import socket
# Test socket.if_indextoname()

from test_support import verbose

iface_name = 'lo'
try:
    sw_if_index = socket.if_nametoindex(iface_name)
except socket.error, err:
    print "could not convert interface name:", err
    import sys
    sys.exit(1)

if (verbose):
    print "Interface Name:", iface_name
    print "Interface Index:", sw_if_index

try:
    if (iface_name == socket.if_indextoname(sw_if_index)):
        print 'OK'
    else:
        print 'Failed'
except socket.error, err:
    print "could not convert interface index:", err
