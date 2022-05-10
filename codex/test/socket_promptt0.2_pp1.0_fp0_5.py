import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    ifname = socket.if_indextoname(1)
    if ifname is None:
        raise TestFailed("if_indextoname(1) returned None")
    if ifname not in socket.if_nameindex():
        raise TestFailed("if_indextoname(1) returned an unknown interface")

# Test socket.if_nameindex()

def test_if_nameindex():
    nlist = socket.if_nameindex()
    if not nlist:
        raise TestFailed("if_nameindex() returned an empty list")
    for i in range(len(nlist)):
        name = nlist[i][0]
        idx = nlist[i][1]
        if socket.if_indextoname(idx) != name:
            raise TestFailed("if_nameindex() returned an invalid name")

# Test socket.getnameinfo()

