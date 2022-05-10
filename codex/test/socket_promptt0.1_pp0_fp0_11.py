import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    ifname = socket.if_indextoname(1)
    if ifname is None:
        raise TestFailed("if_indextoname(1) returned None")
    if ifname not in socket.if_nameindex():
        raise TestFailed("if_indextoname(1) returned an unknown interface name")

# Test socket.if_nameindex()

def test_if_nameindex():
    nlist = socket.if_nameindex()
    if len(nlist) < 1:
        raise TestFailed("if_nameindex() returned an empty list")
    for i in range(len(nlist)):
        name = nlist[i][1]
        ifname = socket.if_indextoname(nlist[i][0])
        if name != ifname:
            raise TestFailed("if_nameindex() returned inconsistent interface name")

# Test socket.if_nametoindex()

def test_if_nametoindex():
    nlist = socket.if_
