import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    ifname = socket.if_indextoname(1)
    assert ifname == 'lo'

def test_if_indextoname_invalid():
    with pytest.raises(OSError):
        socket.if_indextoname(999999)

def test_if_indextoname_none():
    with pytest.raises(OSError):
        socket.if_indextoname(None)

def test_if_indextoname_str():
    with pytest.raises(OSError):
        socket.if_indextoname('1')

def test_if_indextoname_float():
    with pytest.raises(OSError):
        socket.if_indextoname(1.0)

def test_if_indextoname_bytes():
    with pytest.raises(OSError):
        socket.if_indextoname(b'1')

