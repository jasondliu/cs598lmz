import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    if_indextoname = socket.if_indextoname
    try:
        if_indextoname(1)
    except OSError as e:
        if e.errno == errno.ENXIO:
            # No such network interface
            return
        raise
    except AttributeError:
        # Not implemented
        return
    # Should not raise
    if_indextoname(1)
    if_indextoname(1, True)
    if_indextoname(1, False)
    if_indextoname(1, True, True)
    if_indextoname(1, True, False)
    if_indextoname(1, False, True)
    if_indextoname(1, False, False)
    # Should raise
    raises(OSError, if_indextoname, -1)
    raises(OSError, if_indextoname, -1, True)
    raises(OSError, if_indextoname
