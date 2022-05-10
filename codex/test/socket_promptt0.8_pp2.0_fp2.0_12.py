import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    # The socket interface is quite different between POSIX and Windows,
    # so we need specific tests for each in order to test the whole
    # range of values.
    if os.name in ('nt', 'ce'):
        # Windows
        try:
            socket.if_indextoname(socket.INVALID_SOCKET)
        except (OSError, ValueError) as x:
            assert x.errno in (10022, errno.EINVAL)
        else:
            assert False
        try:
            socket.if_indextoname(-10)
        except (OSError, ValueError) as x:
            assert x.errno in (10022, errno.EINVAL)
        else:
            assert False
        try:
            socket.if_indextoname(1000)
        except (OSError, ValueError) as x:
            assert x.errno in (10022, errno.EINVAL)
        else:
            assert False
