import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    assert socket.if_indextoname(1) == 'lo'

def test_if_indextoname_invalid():
    with pytest.raises(OSError):
        socket.if_indextoname(0)

# Test socket.if_nameindex()

def test_if_nameindex():
    assert socket.if_nameindex() == [(1, 'lo')]

# Test socket.if_nametoindex()

def test_if_nametoindex():
    assert socket.if_nametoindex('lo') == 1

def test_if_nametoindex_invalid():
    with pytest.raises(OSError):
        socket.if_nametoindex('eth0')

# Test socket.getaddrinfo()

def test_getaddrinfo():
    assert socket.getaddrinfo('localhost', 80) == [(2, 1, 6, '', ('127.0.0.1', 80))]

def test_getaddrinfo_numeric():
   
