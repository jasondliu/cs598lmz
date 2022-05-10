import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    # This test is Linux-specific.
    if not hasattr(socket, 'if_indextoname'):
        return
    try:
        socket.if_indextoname(1)
    except OSError as e:
        if e.errno == errno.ENXIO:
            # This is what we expect on Linux if there is no interface 1.
            pass
        else:
            raise
    else:
        raise Exception('if_indextoname(1) did not raise ENXIO')
    try:
        socket.if_indextoname(999999)
    except OSError as e:
        if e.errno == errno.ENXIO:
            # This is what we expect on Linux if there is no interface 999999.
            pass
        else:
            raise
    else:
        raise Exception('if_indextoname(999999) did not raise ENXIO')
