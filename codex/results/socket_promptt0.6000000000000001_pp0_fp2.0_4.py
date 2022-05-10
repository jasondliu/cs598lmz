import socket
# Test socket.if_indextoname
def test_socket_if_indextoname():
    # If the index is not valid, an error is raised
    try:
        socket.if_indextoname(0)
    except socket.error:
        pass

# Test socket.if_indextoname
def test_socket_if_indextoname():
    # If the index is valid, a string is returned
    assert isinstance(socket.if_indextoname(socket.if_nametoindex('lo')), str)

# Test socket.if_indextoname
def test_socket_if_indextoname():
    # If the index is valid, a string is returned
    assert isinstance(socket.if_indextoname(socket.if_nametoindex('lo')), str)

# Test socket.if_indextoname
def test_socket_if_indextoname():
    # If the index is not valid, an error is raised
    try:
        socket.if_indextoname(0)
    except socket.error:
        pass

#
