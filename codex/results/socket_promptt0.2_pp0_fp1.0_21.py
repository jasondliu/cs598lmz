import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    # Test if_indextoname()
    #
    # This test is not very good, as it assumes that the first interface
    # has index 1.  This is not always true.
    #
    # Also, it assumes that there is at least one interface.
    #
    # The test is not run if the function is not present.
    #
    if not hasattr(socket, 'if_indextoname'):
        return
    index = 1
    name = socket.if_indextoname(index)
    if not name:
        raise TestFailed, 'if_indextoname(%d) returned null' % index
    if index != socket.if_nametoindex(name):
        raise TestFailed, 'if_nametoindex(if_indextoname(%d)) returned %d' % (
            index, socket.if_nametoindex(name))

test_if_indextoname()

# Test socket.if_nameindex()

def test_if_
