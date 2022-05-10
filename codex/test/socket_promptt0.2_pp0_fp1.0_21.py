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
