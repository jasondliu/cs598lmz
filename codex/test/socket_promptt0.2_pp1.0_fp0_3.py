import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    ifname = socket.if_indextoname(1)
    if ifname is None:
        raise TestFailed("socket.if_indextoname(1) returned None")
    if ifname not in socket.if_nameindex():
        raise TestFailed("socket.if_indextoname(1) returned %s, which doesn't "
                         "appear in socket.if_nameindex()" % ifname)

# Test socket.if_nameindex()

def test_if_nameindex():
    # Test that all the interfaces in the list have valid index numbers
    for ifname, ifindex in socket.if_nameindex():
        if ifindex != socket.if_nametoindex(ifname):
            raise TestFailed("socket.if_nameindex() returned an invalid index "
                             "number for %s" % ifname)

# Test socket.if_nametoindex()

def test_if_nametoindex():
    ifindex = socket.if_nametoindex("lo")
