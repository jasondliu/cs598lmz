import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    # Test if_indextoname()
    ifname = socket.if_indextoname(1)
    if ifname is None:
        raise TestFailed("if_indextoname(1) returned None")
    if ifname not in socket.if_nameindex():
        raise TestFailed("if_indextoname(1) returned invalid interface name")

def test_if_nameindex():
    # Test if_nameindex()
    if_nameindex = socket.if_nameindex()
    if not if_nameindex:
        raise TestFailed("if_nameindex() returned empty list")
    for i, ifname in if_nameindex:
        ifname2 = socket.if_indextoname(i)
        if ifname2 is None:
            raise TestFailed("if_indextoname(%d) returned None" % i)
        if ifname != ifname2:
            raise TestFailed("if_nameindex() and if_indextoname() are inconsistent")
