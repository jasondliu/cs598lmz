import socket
# Test socket.if_indextoname()

from test import support

if not hasattr(socket, 'if_indextoname'):
    raise support.TestSkipped("socket.if_indextoname not defined")


def test_basic():
    # Test basic functionality.
    name = socket.if_indextoname(1)
    index = socket.if_nametoindex(name)
    assert index == 1, (name, index)
    assert socket.if_indextoname(index) == name


def test_errors():
    # Test errors.
    try:
        socket.if_indextoname(-1)
    except OSError as e:
        assert e.errno == errno.EINVAL
    else:
        assert False, "negative index should raise OSError"

    try:
        socket.if_indextoname(0)
    except OSError as e:
        assert e.errno == errno.EINVAL
    else:
        assert False, "zero index should raise OSError"

    try:
       
