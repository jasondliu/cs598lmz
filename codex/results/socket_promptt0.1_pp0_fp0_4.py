import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    ifname = socket.if_indextoname(1)
    if ifname is None:
        raise TestFailed("if_indextoname(1) returned None")
    if ifname not in socket.if_nameindex():
        raise TestFailed("if_indextoname(1) returned an unknown interface")

def test_if_nameindex():
    n = socket.if_nameindex()
    if not n:
        raise TestFailed("if_nameindex() returned empty list")
    for i, ifname in n:
        if socket.if_indextoname(i) != ifname:
            raise TestFailed("if_nameindex() returned bad result")

def test_if_nametoindex():
    ifname = socket.if_nameindex()[0][1]
    if socket.if_nametoindex(ifname) == 0:
        raise TestFailed("if_nametoindex() returned zero")

def test_if_nameindex_cache():
    n =
