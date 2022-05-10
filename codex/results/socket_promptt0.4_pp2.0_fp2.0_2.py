import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    try:
        socket.if_indextoname(0)
    except (OSError, ValueError):
        # No network devices available
        pass
    else:
        # At least one network device available
        assert socket.if_indextoname(socket.if_nametoindex('lo')) == 'lo'

# Test socket.if_nameindex()

def test_if_nameindex():
    try:
        socket.if_nameindex()
    except (OSError, ValueError):
        # No network devices available
        pass
    else:
        # At least one network device available
        assert socket.if_nameindex()

# Test socket.if_nameindex()

def test_if_nameindex():
    try:
        socket.if_nameindex()
    except (OSError, ValueError):
        # No network devices available
        pass
    else:
        # At least one network device available
        assert socket.if_nameindex()

# Test socket.if_nametoindex
