import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    if_indextoname = socket.if_indextoname
    if_indextoname(1)

    raises(OSError, if_indextoname, -1)
    raises(OSError, if_indextoname, 123456789)

def test_if_nameindex():
    if_nameindex = socket.if_nameindex

    # if_nameindex() should return a list of (if_index, if_name) tuples
    for if_index, if_name in if_nameindex():
        assert if_index >= 0
        assert if_name is not None

def test_if_nameindex_empty():
    if_nameindex = socket.if_nameindex

    # if_nameindex() should return an empty list if there are no interfaces
    assert if_nameindex() == []

def test_if_nametoindex():
    if_nametoindex = socket.if_nametoindex

    # if_nametoindex() should return an integer
    assert if_nam
