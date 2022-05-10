import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    if_indextoname = socket.if_indextoname
    try:
        if_indextoname(1)
    except OSError as e:
        if e.errno == errno.EINVAL:
            # No interface with index 1
            pass
        else:
            raise
    else:
        # Interface with index 1 exists
        pass

# Test socket.if_nameindex()

def test_if_nameindex():
    if_nameindex = socket.if_nameindex
    nameindex = if_nameindex()
    for index, name in nameindex:
        if_indextoname(index)
        assert name == if_indextoname(index)

# Test socket.if_nametoindex()

def test_if_nametoindex():
    if_nametoindex = socket.if_nametoindex
    if_nameindex = socket.if_nameindex
    nameindex = if_nameindex()
