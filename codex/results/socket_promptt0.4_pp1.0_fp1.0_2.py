import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    # The if_indextoname() function is not supported on all platforms.
    try:
        socket.if_indextoname(1)
    except socket.error:
        pass
    else:
        # if_indextoname() is supported, check it returns a string
        assert isinstance(socket.if_indextoname(1), str)


def test_if_nameindex():
    # if_nameindex() is supported, check it returns a list of tuples
    assert isinstance(socket.if_nameindex(), list)
    assert isinstance(socket.if_nameindex()[0], tuple)


def test_if_nametoindex():
    # The if_nametoindex() function is not supported on all platforms.
    try:
        socket.if_nametoindex('lo')
    except socket.error:
        pass
    else:
        # if_nametoindex() is supported, check it returns an integer
        assert isinstance(socket.if_nametoindex('lo'), int
