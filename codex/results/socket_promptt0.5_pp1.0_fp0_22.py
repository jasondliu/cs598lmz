import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    # Get the list of all interfaces
    ifnames = socket.if_indextoname(list(range(socket.if_nametoindex('lo'))))
    # Check that the list of interfaces is non-empty
    assert ifnames, 'No interfaces found'
    # Check that the loopback interface is in the list
    assert 'lo' in ifnames, 'Loopback interface not found'
    # Check that the index of the loopback interface is zero
    assert socket.if_nametoindex('lo') == 0, 'Loopback interface index not zero'
    # Check that the loopback interface can be looked up by index
    assert socket.if_indextoname(0) == 'lo', 'Loopback interface not found by index'
