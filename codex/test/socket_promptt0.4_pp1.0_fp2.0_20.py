import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    try:
        socket.if_indextoname(1)
    except OSError as e:
        if e.errno == errno.ENXIO:
            pass
        else:
            raise
    else:
        raise

# Test socket.if_nametoindex()

def test_if_nametoindex():
    try:
        socket.if_nametoindex('lo')
    except OSError as e:
        if e.errno == errno.ENXIO:
            pass
        else:
            raise
    else:
        raise

# Test socket.if_nameindex()

def test_if_nameindex():
    try:
        socket.if_nameindex()
    except OSError as e:
        if e.errno == errno.ENXIO:
            pass
        else:
            raise
    else:
        raise

# Test socket.if_freenameindex()

