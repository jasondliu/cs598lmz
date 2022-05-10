import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    # This test requires a network interface.
    if not hasattr(socket, 'if_indextoname'):
        return
    try:
        socket.if_indextoname(1)
    except OSError:
        pass
    else:
        assert False, 'expected OSError'
