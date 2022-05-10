import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    if_indextoname = socket.if_indextoname
    if_indextoname(0)
    raises(OverflowError, if_indextoname, 2**32)
    raises(OverflowError, if_indextoname, -1)
    raises(OSError, if_indextoname, 2**32-1)
    raises(OSError, if_indextoname, -1)
    raises(TypeError, if_indextoname)
    raises(TypeError, if_indextoname, "foo")
    raises(TypeError, if_indextoname, 1, 2, 3)
