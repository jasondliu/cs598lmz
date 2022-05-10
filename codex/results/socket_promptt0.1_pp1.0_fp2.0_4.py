import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    ifname = socket.if_indextoname(1)
    assert ifname == 'lo'

def test_if_indextoname_error():
    with pytest.raises(OSError):
        socket.if_indextoname(9999)

def test_if_indextoname_error_msg():
    try:
        socket.if_indextoname(9999)
    except OSError as e:
        assert e.args[0] == 99

def test_if_indextoname_error_msg_str():
    try:
        socket.if_indextoname(9999)
    except OSError as e:
        assert str(e) == '[Errno 99] Network is unreachable'

# Test socket.if_nameindex()

def test_if_nameindex():
    ifname = socket.if_nameindex()
    assert ifname == [(1, 'lo')]

# Test socket.if_nameindex()

def
