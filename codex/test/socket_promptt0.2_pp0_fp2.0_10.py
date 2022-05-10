import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    assert socket.if_indextoname(1) == 'lo'
    assert socket.if_indextoname(2) == 'eth0'
    assert socket.if_indextoname(3) == 'wlan0'

# Test socket.if_nameindex()

def test_if_nameindex():
    assert socket.if_nameindex() == [(1, 'lo'), (2, 'eth0'), (3, 'wlan0')]

# Test socket.if_nametoindex()

def test_if_nametoindex():
    assert socket.if_nametoindex('lo') == 1
    assert socket.if_nametoindex('eth0') == 2
    assert socket.if_nametoindex('wlan0') == 3

# Test socket.getaddrinfo()

def test_getaddrinfo():
    assert socket.getaddrinfo('localhost', 80) == [(2, 1, 6, '', ('127.0.0.1', 80))]
    assert socket.get
