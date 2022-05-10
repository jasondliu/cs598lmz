import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    """
    Test socket.if_indextoname()
    """
    try:
        socket.if_indextoname(1)
    except socket.error:
        pass
    else:
        raise Exception("socket.if_indextoname() should raise socket.error")

# Test socket.if_nameindex()

def test_if_nameindex():
    """
    Test socket.if_nameindex()
    """
    try:
        socket.if_nameindex()
    except socket.error:
        pass
    else:
        raise Exception("socket.if_nameindex() should raise socket.error")

# Test socket.if_nametoindex()

def test_if_nametoindex():
    """
    Test socket.if_nametoindex()
    """
    try:
        socket.if_nametoindex("lo")
    except socket.error:
        pass
    else:
        raise Exception("socket.if_nametoindex() should raise socket.error")


