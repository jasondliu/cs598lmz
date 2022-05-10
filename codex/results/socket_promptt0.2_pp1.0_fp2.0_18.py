import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    try:
        socket.if_indextoname(0)
    except OSError as e:
        if e.errno == errno.EINVAL:
            # No interface with index 0
            return
        raise
    else:
        # We have an interface with index 0
        pass
