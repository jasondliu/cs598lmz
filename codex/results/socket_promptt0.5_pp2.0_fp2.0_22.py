import socket
# Test socket.if_indextoname()
#
# Also see test_socket.py for more socket tests.
#
# Skip these tests if the platform does not have enough interfaces.

def test_if_indextoname():
    import socket
    try:
        socket.if_indextoname(1)
    except ValueError:
        pass
    else:
        raise AssertionError("should have raised ValueError")

def test_if_indextoname2():
    import socket
    try:
        socket.if_indextoname(1)
    except ValueError:
        pass
    else:
        raise AssertionError("should have raised ValueError")

def test_if_indextoname3():
    import socket
    try:
        socket.if_indextoname(-1)
    except ValueError:
        pass
    else:
        raise AssertionError("should have raised ValueError")

def test_if_indextoname4():
    import socket
    try:
        socket.if_indextoname(0)
    except ValueError:
