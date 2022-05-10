import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    """Test socket.if_indextoname()."""
    ifname = socket.if_indextoname(1)
    if ifname is None:
        raise TestFailed("if_indextoname(1) failed")
    if socket.if_indextoname(1) != ifname:
        raise TestFailed("if_indextoname(1) failed")
    if socket.if_indextoname(2) != 'lo':
        raise TestFailed("if_indextoname(2) failed")
    if socket.if_indextoname(3) is not None:
        raise TestFailed("if_indextoname(3) failed")
    if socket.if_indextoname(-1) is not None:
        raise TestFailed("if_indextoname(-1) failed")

# Test socket.if_nameindex()

def test_if_nameindex():
    """Test socket.if_nameindex()."""
