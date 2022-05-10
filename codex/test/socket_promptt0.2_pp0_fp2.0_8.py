import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    ifname = socket.if_indextoname(1)
    assert ifname == 'lo'

def test_if_indextoname_error():
    with pytest.raises(OSError):
        socket.if_indextoname(0)

# Test socket.if_nameindex()

def test_if_nameindex():
    ifname = socket.if_nameindex()
    assert ifname == [(1, 'lo')]

# Test socket.if_nametoindex()

def test_if_nametoindex():
    ifindex = socket.if_nametoindex('lo')
    assert ifindex == 1

def test_if_nametoindex_error():
    with pytest.raises(OSError):
        socket.if_nametoindex('eth0')
