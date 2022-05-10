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
        socket.if_indextoname(100)

# Test socket.if_nameindex()

def test_if_nameindex():
    ifname = socket.if_nameindex()
    assert ifname[0][0] == 1
    assert ifname[0][1] == 'lo'

# Test socket.if_nametoindex()

def test_if_nametoindex():
    ifname = socket.if_nametoindex('lo')
    assert ifname == 1

def test_if_nametoindex_error():
    with pytest.raises(OSError):
        socket.if_nametoindex
