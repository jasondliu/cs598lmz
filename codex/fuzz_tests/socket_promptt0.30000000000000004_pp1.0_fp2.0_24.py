import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    """Test socket.if_indextoname()"""
    # This test is not very good.  It just makes sure that
    # if_indextoname() doesn't blow up.
    socket.if_indextoname(1)

def test_if_nameindex():
    """Test socket.if_nameindex()"""
    # This test is not very good.  It just makes sure that
    # if_nameindex() doesn't blow up.
    socket.if_nameindex()

def test_if_nametoindex():
    """Test socket.if_nametoindex()"""
    # This test is not very good.  It just makes sure that
    # if_nametoindex() doesn't blow up.
    socket.if_nametoindex('lo')

def test_gethostbyname():
    """Test socket.gethostbyname()"""
    # This test is not very good.  It just makes sure that
    # gethostbyname() doesn't blow up.
    socket.gethostby
