import socket
# Test socket.if_indextoname

def test_if_indextoname():
    ifname = socket.if_indextoname(1)
    if ifname is None:
        raise TestFailed("if_indextoname(1) should not return None")
    if not isinstance(ifname, str):
        raise TestFailed("if_indextoname(1) should return a string, not %s" %
                         repr(ifname))

# Test socket.if_nameindex

def test_if_nameindex():
    names = socket.if_nameindex()
    if not isinstance(names, list):
        raise TestFailed("if_nameindex() should return a list, not %s" %
                         repr(names))
    for i in names:
        if not isinstance(i, tuple) or len(i) != 2:
            raise TestFailed("if_nameindex() should return a list of 2-tuples")
        if not (isinstance(i[0], int) and isinstance(i[1], str)):
            raise TestFailed("if_name
