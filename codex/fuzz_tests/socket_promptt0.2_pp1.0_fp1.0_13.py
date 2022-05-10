import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    try:
        socket.if_indextoname(1)
    except socket.error:
        pass
    else:
        assert False, 'Expected socket.error'

# Test socket.if_nameindex()

def test_if_nameindex():
    try:
        socket.if_nameindex()
    except socket.error:
        pass
    else:
        assert False, 'Expected socket.error'

# Test socket.if_nametoindex()

def test_if_nametoindex():
    try:
        socket.if_nametoindex('lo')
    except socket.error:
        pass
    else:
        assert False, 'Expected socket.error'

# Test socket.getaddrinfo()

def test_getaddrinfo():
    try:
        socket.getaddrinfo('localhost', 80)
    except socket.error:
        pass
    else:
        assert False, 'Expected socket.error'

# Test socket.getnameinfo()

def
