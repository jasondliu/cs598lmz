import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    # Test if_indextoname() for a valid interface index.
    assert socket.if_indextoname(1) == 'lo'

    # Test if_indextoname() for invalid interface index.
    with pytest.raises(OSError):
        socket.if_indextoname(0)
    with pytest.raises(OSError):
        socket.if_indextoname(2**32)

def test_if_indextoname_exception():
    # Test if_indextoname() for invalid interface index.
    with pytest.raises(OSError):
        socket.if_indextoname(0)
    with pytest.raises(OSError):
        socket.if_indextoname(2**32)

def test_if_indextoname_type():
    # Test if_indextoname() for invalid type of interface index.
    with pytest.raises(TypeError):
        socket.if_indextoname(None
