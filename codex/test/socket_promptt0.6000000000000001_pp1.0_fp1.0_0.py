import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    try:
        socket.if_indextoname(0)
    except OSError as e:
        assert e.args[0] == errno.EINVAL
    else:
        raise Exception("expected OSError(EINVAL)")

