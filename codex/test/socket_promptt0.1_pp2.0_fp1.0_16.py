import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    # Test if_indextoname()
    if_indextoname = socket.if_indextoname
    try:
        if_indextoname(1)
    except OSError as e:
        if e.errno == errno.EINVAL:
            # Invalid argument
            pass
        else:
            raise
    else:
        # No exception raised
        pass

# Test socket.if_nameindex()

def test_if_nameindex():
    # Test if_nameindex()
    if_nameindex = socket.if_nameindex
    try:
        if_nameindex()
    except OSError as e:
        if e.errno == errno.EINVAL:
            # Invalid argument
            pass
        else:
            raise
    else:
        # No exception raised
        pass

# Test socket.if_nametoindex()

def test_if_nametoindex():
    # Test if_nametoindex()
    if_nameto
