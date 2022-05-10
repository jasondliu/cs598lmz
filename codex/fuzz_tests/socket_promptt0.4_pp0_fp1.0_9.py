import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    # Test basic functionality
    assert socket.if_indextoname(1) == 'lo'

    # Test invalid arguments
    assert socket.if_indextoname(0) is None
    assert socket.if_indextoname(-1) is None
    assert socket.if_indextoname(1.0) is None
    assert socket.if_indextoname(None) is None
    assert socket.if_indextoname('1') is None
    assert socket.if_indextoname(b'1') is None

# Test socket.if_nameindex()

def test_if_nameindex():
    # Test basic functionality
    assert socket.if_nameindex()[0] == (1, 'lo')

    # Test invalid arguments
    assert socket.if_nameindex(None) == []
    assert socket.if_nameindex(1) == []
    assert socket.if_nameindex(1.0) == []
    assert socket.if_nameindex('1') == []

