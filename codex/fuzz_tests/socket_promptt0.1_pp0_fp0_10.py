import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    # Test if_indextoname()
    ifname = socket.if_indextoname(1)
    if not ifname:
        raise TestFailed("if_indextoname(1) failed")
    if ifname not in socket.if_nameindex():
        raise TestFailed("if_indextoname(1) returned invalid name")

def test_if_nameindex():
    # Test if_nameindex()
    names = [name for (index, name) in socket.if_nameindex()]
    if not names:
        raise TestFailed("if_nameindex() failed")
    for name in names:
        if not socket.if_indextoname(socket.if_nametoindex(name)):
            raise TestFailed("if_nameindex() returned invalid name")

def test_if_nametoindex():
    # Test if_nametoindex()
    if socket.if_nametoindex('lo') != 1:
        raise TestFailed("if_nametoindex
