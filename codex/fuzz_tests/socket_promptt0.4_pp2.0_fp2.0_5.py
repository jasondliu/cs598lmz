import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    # get all interface indices
    indices = socket.if_indices()
    for index in indices:
        # get name for each index
        name = socket.if_indextoname(index)
        # verify that name is valid
        assert name == socket.if_indextoname(index)

# Test socket.if_nameindex()

def test_if_nameindex():
    # get all interface names
    names = socket.if_nameindex()
    for name, index in names:
        # verify that index is valid
        assert index == socket.if_nametoindex(name)

# Test socket.if_nametoindex()

def test_if_nametoindex():
    # get all interface names
    names = socket.if_nameindex()
    for name, index in names:
        # verify that index is valid
        assert index == socket.if_nametoindex(name)

# Test socket.if_nameindex()

def test_if_nameindex():
    # get all
