import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    try:
        socket.if_indextoname(1)
    except OSError:
        pass
    else:
        print('socket.if_indextoname() should fail')

# Test socket.if_nameindex()

def test_if_nameindex():
    try:
        socket.if_nameindex()
    except OSError:
        pass
    else:
        print('socket.if_nameindex() should fail')

# Test socket.if_nametoindex()

def test_if_nametoindex():
    try:
        socket.if_nametoindex('lo')
    except OSError:
        pass
    else:
        print('socket.if_nametoindex() should fail')

# Test socket.gethostbyname_ex()

def test_gethostbyname_ex():
    try:
        socket.gethostbyname_ex('localhost')
    except OSError:
        pass
