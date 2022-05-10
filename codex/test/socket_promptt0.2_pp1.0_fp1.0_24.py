import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    if_indextoname = socket.if_indextoname
    if_indextoname(1)
    if_indextoname(1, 'foo')
    raises(OverflowError, if_indextoname, 2**32)
    raises(OverflowError, if_indextoname, -1)
    raises(TypeError, if_indextoname, 'foo')
    raises(TypeError, if_indextoname, 1, 1)
    raises(TypeError, if_indextoname, 1, b'foo')

# Test socket.if_nameindex()

def test_if_nameindex():
    if_nameindex = socket.if_nameindex
    if_nameindex()
    if_nameindex(1)
    raises(TypeError, if_nameindex, 'foo')

# Test socket.if_nametoindex()

def test_if_nametoindex():
    if_nametoindex = socket.if_nametoindex
    if_nam
