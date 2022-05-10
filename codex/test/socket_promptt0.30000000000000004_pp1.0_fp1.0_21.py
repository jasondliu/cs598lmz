import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    try:
        socket.if_indextoname(1)
    except OSError:
        pass
    else:
        raise Exception("should have raised OSError")

# Test socket.if_nameindex()

def test_if_nameindex():
    try:
        socket.if_nameindex()
    except OSError:
        pass
    else:
        raise Exception("should have raised OSError")

# Test socket.if_nametoindex()

def test_if_nametoindex():
    try:
        socket.if_nametoindex("lo")
    except OSError:
        pass
    else:
        raise Exception("should have raised OSError")

# Test socket.sethostname()

def test_sethostname():
    try:
        socket.sethostname("micropython")
    except OSError:
        pass
    else:
        raise Exception("should have raised OSError")

# Test socket
