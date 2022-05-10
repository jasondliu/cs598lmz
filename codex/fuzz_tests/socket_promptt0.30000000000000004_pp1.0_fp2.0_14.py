import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    if_indextoname = socket.if_indextoname
    if_indextoname(1)
    if_indextoname(1, 'xx')

def test_if_indextoname_error():
    if_indextoname = socket.if_indextoname
    raises(OverflowError, if_indextoname, -1)
    raises(OverflowError, if_indextoname, 2**31)
    raises(TypeError, if_indextoname, 1, 1)
    raises(TypeError, if_indextoname, 1, 'xx', 'xx')

def test_if_nameindex():
    if_nameindex = socket.if_nameindex
    if_nameindex()
    if_nameindex(1)
    if_nameindex(1, 'xx')

def test_if_nameindex_error():
    if_nameindex = socket.if_nameindex
    raises(TypeError, if_nameindex, 1, 1)
