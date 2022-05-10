import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    ifname = socket.if_indextoname(1)
    assert ifname == 'lo'

# Test socket.if_nameindex()

def test_if_nameindex():
    ifnames = socket.if_nameindex()
    assert ifnames[0] == (1, 'lo')

# Test socket.if_nametoindex()

def test_if_nametoindex():
    ifindex = socket.if_nametoindex('lo')
    assert ifindex == 1

# Test socket.getaddrinfo()

def test_getaddrinfo():
    addrinfo = socket.getaddrinfo('localhost', 80)
    assert addrinfo[0] == (2, 1, 6, '', ('127.0.0.1', 80))

# Test socket.getnameinfo()

def test_getnameinfo():
    nameinfo = socket.getnameinfo(('127.0.0.1', 80), 0)
    assert nameinfo == ('localhost', 'http')

# Test socket.
