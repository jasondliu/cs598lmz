import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    assert hasattr(socket, 'if_indextoname')
    assert callable(socket.if_indextoname)

    # Test invalid arguments.
    assert_raises(OverflowError, socket.if_indextoname, -1)
    assert_raises(OverflowError, socket.if_indextoname, 256)
    assert_raises(TypeError, socket.if_indextoname, '')
    assert_raises(TypeError, socket.if_indextoname, 'a')
    assert_raises(TypeError, socket.if_indextoname, b'a')
    assert_raises(TypeError, socket.if_indextoname, None)

    # Test valid arguments.
    assert socket.if_indextoname(0)
    assert socket.if_indextoname(1)
    assert socket.if_indextoname(255)

