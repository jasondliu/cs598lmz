import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    # test error conditions
    try:
        socket.if_indextoname(-1)
    except ValueError:
        pass
    else:
        raise Exception, 'expected ValueError'
    try:
        socket.if_indextoname(2**16)
    except ValueError:
        pass
    else:
        raise Exception, 'expected ValueError'

    # test success conditions
    socket.if_indextoname(0)
    socket.if_indextoname(1)
    socket.if_indextoname(2**16 - 1)

# Test socket.if_nameindex()

def test_if_nameindex():
    # test success conditions
    socket.if_nameindex()

# Test socket.if_nametoindex()

def test_if_nametoindex():
    # test error conditions
    try:
        socket.if_nametoindex('lo0')
    except ValueError:
        pass
    else:
        raise Exception, 'expected ValueError'
