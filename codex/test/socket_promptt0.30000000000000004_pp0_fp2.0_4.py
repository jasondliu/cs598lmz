import socket
# Test socket.if_indextoname
if_indextoname = socket.if_indextoname

def test_if_indextoname():
    assert if_indextoname(1) == 'lo'

# Test socket.if_nameindex
if_nameindex = socket.if_nameindex

def test_if_nameindex():
    assert if_nameindex()[0] == (1, 'lo')

# Test socket.if_nametoindex
if_nametoindex = socket.if_nametoindex

def test_if_nametoindex():
    assert if_nametoindex('lo') == 1

# Test socket.gethostbyname
gethostbyname = socket.gethostbyname

def test_gethostbyname():
    assert gethostbyname('localhost') == '127.0.0.1'

# Test socket.gethostbyname_ex
gethostbyname_ex = socket.gethostbyname_ex

