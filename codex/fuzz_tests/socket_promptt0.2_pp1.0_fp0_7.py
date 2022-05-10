import socket
# Test socket.if_indextoname()

def test_if_indextoname(dev, family):
    ifname = socket.if_indextoname(dev)
    if ifname is None:
        print('if_indextoname(%d) returned None' % dev)
    else:
        print('if_indextoname(%d) = %s' % (dev, ifname))
        if socket.if_nametoindex(ifname) != dev:
            print('if_nametoindex(%s) = %d' % (ifname, socket.if_nametoindex(ifname)))

test_if_indextoname(0, socket.AF_INET)
test_if_indextoname(1, socket.AF_INET)
test_if_indextoname(2, socket.AF_INET)
test_if_indextoname(3, socket.AF_INET)
test_if_indextoname(4, socket.AF_INET)
test_if_indextoname(5, socket.AF_INET)
