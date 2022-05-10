import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    try:
        socket.if_indextoname(0)
    except OSError:
        pass

# Test socket.if_nameindex()

def test_if_nameindex():
    try:
        socket.if_nameindex()
    except OSError:
        pass

# Test socket.if_nametoindex()

def test_if_nametoindex():
    try:
        socket.if_nametoindex('lo')
    except OSError:
        pass

# Test socket.gethostbyname_ex()

def test_gethostbyname_ex():
    socket.gethostbyname_ex('localhost')
    try:
        socket.gethostbyname_ex('')
    except socket.error:
        pass

# Test socket.gethostbyaddr()

def test_gethostbyaddr():
    socket.gethostbyaddr('127.0.0.1')
