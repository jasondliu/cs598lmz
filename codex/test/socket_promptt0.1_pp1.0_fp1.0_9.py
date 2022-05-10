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
        socket.if_indextoname(9999)

def test_if_indextoname_error3():
    with pytest.raises(OSError):
        socket.if_indextoname(-1)

def test_if_indextoname_error4():
    with pytest.raises(TypeError):
        socket.if_indextoname('1')

def test_if_indextoname_error5():
    with pytest.raises(TypeError):
        socket.if_indextoname(1.0)

