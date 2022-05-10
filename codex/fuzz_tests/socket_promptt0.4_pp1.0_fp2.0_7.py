import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    # This test may fail if the machine has no interfaces configured,
    # or if all the interfaces are "down"
    try:
        socket.if_indextoname(1)
    except ValueError:
        pass
    else:
        raise TestFailed("if_indextoname(1) didn't raise ValueError")

    # This should work on any machine with at least one interface
    try:
        socket.if_indextoname(0)
    except ValueError:
        raise TestFailed("if_indextoname(0) raised ValueError")

# Test socket.if_nameindex()

def test_if_nameindex():
    try:
        l = socket.if_nameindex()
    except ValueError:
        pass
    else:
        if len(l) < 1:
            raise TestFailed("if_nameindex() didn't return anything")
        # The list returned by if_nameindex() should contain a series
        # of (index, name) tuples
        for
