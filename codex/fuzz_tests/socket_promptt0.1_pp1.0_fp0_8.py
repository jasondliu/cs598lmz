import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    # Test if_indextoname()
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

def test_if_nameindex():
    # Test if_nameindex()
    if_nameindex = socket.if_nameindex
    for index, name in if_nameindex():
        if_indextoname(index)
        assert name == if_indextoname(index)

def test_if_nameindex_exception():
    # Test if_nameindex() exception
    if_nameindex = socket.if_nameindex
    try:
        if_nameindex(-1)
    except OSError as e:
        if e.errno == errno.EIN
