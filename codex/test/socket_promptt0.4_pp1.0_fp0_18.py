import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    try:
        socket.if_indextoname(1)
    except OSError:
        pass
    else:
        assert False, 'if_indextoname() should raise OSError'

# Test socket.if_indextoname()

def test_if_indextoname():
    try:
        socket.if_indextoname(1)
    except OSError:
        pass
    else:
        assert False, 'if_indextoname() should raise OSError'

# Test socket.if_nameindex()

def test_if_nameindex():
    try:
        socket.if_nameindex()
    except OSError:
        pass
    else:
        assert False, 'if_nameindex() should raise OSError'

# Test socket.if_nametoindex()

