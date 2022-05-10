import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    assert socket.if_indextoname(1) == 'lo'

def test_if_indextoname_invalid():
    try:
        socket.if_indextoname(100)
    except OSError:
        pass
    else:
        raise Exception("Expected OSError")

# Test socket.if_nameindex()

def test_if_nameindex():
    assert socket.if_nameindex() == [(1, 'lo')]

# Test socket.if_nametoindex()

def test_if_nametoindex():
    assert socket.if_nametoindex('lo') == 1

def test_if_nametoindex_invalid():
    try:
        socket.if_nametoindex('invalid')
    except OSError:
        pass
    else:
        raise Exception("Expected OSError")

# Test socket.gethostbyname()

def test_gethostbyname():
    assert socket.gethostbyname
