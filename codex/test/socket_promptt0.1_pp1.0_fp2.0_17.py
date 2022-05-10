import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    ifname = socket.if_indextoname(1)
    assert ifname == 'lo'

def test_if_indextoname_error():
    with pytest.raises(OSError):
        socket.if_indextoname(0)

def test_if_indextoname_error2():
    with pytest.raises(OSError):
        socket.if_indextoname(2**32)

def test_if_indextoname_error3():
    with pytest.raises(OSError):
        socket.if_indextoname(-1)
