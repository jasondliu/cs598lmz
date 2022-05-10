import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    """Test if_indextoname()."""
    assert socket.if_indextoname(0) == 'lo'
    assert socket.if_indextoname(1) == 'eth0'

# Test socket.if_nameindex()

def test_if_nameindex():
    """Test if_nameindex()."""
    if_nameindex = socket.if_nameindex()
    assert if_nameindex[0] == (0, 'lo')
    assert if_nameindex[1] == (1, 'eth0')

# Test socket.if_nametoindex()

def test_if_nametoindex():
    """Test if_nametoindex()."""
    assert socket.if_nametoindex('lo') == 0
    assert socket.if_nametoindex('eth0') == 1
