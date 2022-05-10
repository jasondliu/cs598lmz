import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    # Get all interface indices
    all_indices = set(socket.if_indices())
    # Get all interface names
    all_names = set(socket.if_nameindex())
    # Get all interface names
    all_names = set(socket.if_nameindex())
    # Check that if_indextoname() returns the correct name
    for index, name in all_names:
        assert socket.if_indextoname(index) == name
    # Check that if_indextoname() raises an exception for invalid indices
    for index in all_indices - set(all_names):
        try:
            socket.if_indextoname(index)
        except OSError as e:
            assert e.errno == errno.EINVAL
        else:
            assert False, "Expected OSError"
