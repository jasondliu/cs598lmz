import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    try:
        socket.if_indextoname(1)
    except OSError:
        pass
    else:
        assert False, 'if_indextoname() should fail'

# Test socket.if_nametoindex()

def test_if_nametoindex():
    try:
        socket.if_nametoindex('lo')
    except OSError:
        pass
    else:
        assert False, 'if_nametoindex() should fail'

# Test socket.getaddrinfo()

def test_getaddrinfo():
    try:
        socket.getaddrinfo('localhost', 80)
    except OSError:
        pass
    else:
        assert False, 'getaddrinfo() should fail'

# Test socket.getnameinfo()

def test_getnameinfo():
    try:
        socket.getnameinfo(('127.0.0.1', 80), 0)
    except OSError:
        pass
    else:
        assert
