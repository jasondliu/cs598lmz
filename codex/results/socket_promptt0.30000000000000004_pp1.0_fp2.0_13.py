import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    """
    Test socket.if_indextoname()
    """
    if_indextoname = socket.if_indextoname
    assert if_indextoname(1) == 'lo'
    assert if_indextoname(2) == 'eth0'

def test_if_indextoname_error():
    """
    Test socket.if_indextoname()
    """
    if_indextoname = socket.if_indextoname
    raises(OSError, if_indextoname, -1)
    raises(OSError, if_indextoname, 0)
    raises(OSError, if_indextoname, 3)

# Test socket.if_nameindex()

def test_if_nameindex():
    """
    Test socket.if_nameindex()
    """
    if_nameindex = socket.if_nameindex
    assert if_nameindex() == [(1, 'lo'), (2, 'eth0')]

#
