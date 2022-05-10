import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    # Test if_indextoname()
    #
    # This test is not very good, because it assumes that there is at least
    # one interface, and that it has index 1.  This is true for most
    # machines, but not all.

    # Get the interface name of index 1
    name = socket.if_indextoname(1)
    # Get the interface index of name
    index = socket.if_nametoindex(name)
    # Check that the index is correct
    assert index == 1, "if_indextoname() failed"

def test_if_nameindex():
    # Test if_nameindex()
    #
    # This test is not very good, because it assumes that there is at least
    # one interface, and that it has index 1.  This is true for most
    # machines, but not all.

    # Get the interface name of index 1
    name = socket.if_indextoname(1)
    # Get the interface index of name
    index = socket.
