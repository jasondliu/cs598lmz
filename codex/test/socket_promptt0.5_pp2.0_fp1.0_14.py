import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    ifname = socket.if_indextoname(1)
    assert ifname == 'lo', ifname
    assert socket.if_indextoname(1000) is None

def test_if_indextoname_error():
    raises(OverflowError, socket.if_indextoname, -1)
    raises(OverflowError, socket.if_indextoname, 1<<32)

def test_if_nameindex():
    assert socket.if_nameindex() != []
    assert socket.if_nameindex() != None

def test_if_nameindex_error():
    raises(ValueError, socket.if_nameindex, -1)
    raises(OverflowError, socket.if_nameindex, 1<<32)
