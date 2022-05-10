import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    ifname = socket.if_indextoname(1)
    assert ifname == 'lo', ifname

def test_if_indextoname_error():
    raises(OverflowError, socket.if_indextoname, -1)
    raises(OverflowError, socket.if_indextoname, 2**32)

def test_if_indextoname_non_existing():
    raises(OSError, socket.if_indextoname, 2**32)

def test_if_nameindex():
    iflist = socket.if_nameindex()
    assert iflist[0] == (1, 'lo'), iflist

def test_if_nameindex_error():
    raises(OverflowError, socket.if_nameindex, -1)
    raises(OverflowError, socket.if_nameindex, 2**32)

def test_if_nameindex_non_existing():
    raises(OSError, socket.if_nameindex, 2**32)
