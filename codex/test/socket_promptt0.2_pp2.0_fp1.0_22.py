import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    ifname = socket.if_indextoname(1)
    assert ifname == 'lo'

def test_if_indextoname_error():
    with pytest.raises(OSError):
        socket.if_indextoname(9999)

def test_if_indextoname_error2():
    with pytest.raises(OSError):
        socket.if_indextoname(-1)

# Test socket.if_nameindex()

def test_if_nameindex():
    ifs = socket.if_nameindex()
    assert ifs[0][0] == 1
    assert ifs[0][1] == 'lo'

# Test socket.if_nametoindex()

def test_if_nametoindex():
    index = socket.if_nametoindex('lo')
    assert index == 1

