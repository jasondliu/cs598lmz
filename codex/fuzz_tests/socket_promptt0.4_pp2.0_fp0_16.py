import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    # Interface indices are platform-dependent, so we can't
    # verify the result
    socket.if_indextoname(1)

def test_if_indextoname_exception():
    raises(ValueError, socket.if_indextoname, -1)
