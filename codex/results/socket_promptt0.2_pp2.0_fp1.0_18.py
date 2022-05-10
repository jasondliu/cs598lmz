import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    assert socket.if_indextoname(1) == 'lo'

# Test socket.if_nameindex()

def test_if_nameindex():
    assert socket.if_nameindex() == [(1, 'lo')]

# Test socket.if_nametoindex()

def test_if_nametoindex():
    assert socket.if_nametoindex('lo') == 1

# Test socket.gethostbyname()

def test_gethostbyname():
    assert socket.gethostbyname('localhost') == '127.0.0.1'

# Test socket.gethostbyname_ex()

def test_gethostbyname_ex():
    assert socket.gethostbyname_ex('localhost') == ('localhost', [], ['127.0.0.1'])

# Test socket.gethostname()

def test_gethostname():
    assert socket.gethostname() == 'localhost'

# Test socket.gethostbyaddr()

def test_get
