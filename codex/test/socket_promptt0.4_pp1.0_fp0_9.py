import socket
# Test socket.if_indextoname

def test_if_indextoname():
    assert socket.if_indextoname(1) == 'lo'

# Test socket.if_nameindex

def test_if_nameindex():
    assert socket.if_nameindex()[0] == (1, 'lo')

# Test socket.if_nametoindex

def test_if_nametoindex():
    assert socket.if_nametoindex('lo') == 1

# Test socket.getaddrinfo

def test_getaddrinfo():
    assert socket.getaddrinfo('localhost', 80) == [(2, 1, 6, '', ('127.0.0.1', 80))]

# Test socket.gethostbyname

def test_gethostbyname():
    assert socket.gethostbyname('localhost') == '127.0.0.1'

# Test socket.gethostbyname_ex

