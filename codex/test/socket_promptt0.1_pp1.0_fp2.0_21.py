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
    ifindex = socket.if_nametoindex(socket.if_indextoname(1))
    if ifindex != 1:
        raise TestFailed("if_nametoindex(if_indextoname(1)) returned %d, expected 1" % ifindex)

def test_if_nameindex_errors():
    # Test if_nameindex() errors
    try:
        socket.if_nametoindex('')
    except ValueError:
        pass
