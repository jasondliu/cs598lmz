import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    ifname = socket.if_indextoname(1)
    if ifname is None:
        raise TestFailed, "if_indextoname(1) returned None"
    if ifname not in socket.if_nameindex():
        raise TestFailed, "if_indextoname(1) returned an unknown interface"

def test_if_nameindex():
    # Test that all returned interfaces are known to the system
    for (index, name) in socket.if_nameindex():
        ifname = socket.if_indextoname(index)
        if ifname != name:
            raise TestFailed, "if_nameindex() returned (%d, %s) but " \
                              "if_indextoname(%d) returned %s" % \
                              (index, name, index, ifname)

def test_if_nametoindex():
    # Test that all returned interfaces are known to the system
    for (index, name) in socket.if_nameindex():
        if
