import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    """Test socket.if_indextoname()"""
    if_indextoname = socket.if_indextoname
    if_indextoname(1)

def test_if_nameindex():
    """Test socket.if_nameindex()"""
    if_nameindex = socket.if_nameindex
    if_nameindex()

def test_if_nametoindex():
    """Test socket.if_nametoindex()"""
    if_nametoindex = socket.if_nametoindex
    if_nametoindex('lo')

def test_gethostbyname_ex():
    """Test socket.gethostbyname_ex()"""
    gethostbyname_ex = socket.gethostbyname_ex
    gethostbyname_ex('localhost')

def test_getnameinfo():
    """Test socket.getnameinfo()"""
    getnameinfo = socket.getnameinfo
    getnameinfo(('127.0.0.1', 0), 0)

