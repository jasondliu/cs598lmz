import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    assert socket.if_indextoname(1) == 'lo'

def test_if_indextoname_exception():
    with pytest.raises(OSError):
        socket.if_indextoname(0)

def test_if_indextoname_exception_msg():
    with pytest.raises(OSError) as excinfo:
        socket.if_indextoname(0)
    assert "interface index 0 doesn't exist" in str(excinfo.value)

# Test socket.if_nameindex()

def test_if_nameindex():
    assert socket.if_nameindex() == [(1, 'lo')]

# Test socket.if_nametoindex()

def test_if_nametoindex():
    assert socket.if_nametoindex('lo') == 1

def test_if_nametoindex_exception():
    with pytest.raises(OSError):
        socket.if_nametoindex('eth0')

