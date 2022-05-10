import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    """ Test socket.if_indextoname() """
    # Test that an exception is raised if the interface index is invalid
    try:
        socket.if_indextoname(0)
    except ValueError:
        pass
    else:
        raise AssertionError("socket.if_indextoname() did not raise ValueError")
    # Test that an exception is raised if the interface index is invalid
    try:
        socket.if_indextoname(-1)
    except ValueError:
        pass
    else:
        raise AssertionError("socket.if_indextoname() did not raise ValueError")
    # Test that the interface name is returned for a valid interface index
    # (assuming that the machine has at least one interface)
    socket.if_indextoname(1)

if __name__ == '__main__':
    test_if_indextoname()
