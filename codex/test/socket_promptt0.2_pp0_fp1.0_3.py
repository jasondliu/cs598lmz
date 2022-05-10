import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    """
    Test socket.if_indextoname()
    """
    # Get the interface index
    if_index = socket.if_nametoindex("lo")
    # Get the interface name
    if_name = socket.if_indextoname(if_index)
    # Check if the interface name is correct
    assert if_name == "lo"

# Test socket.if_nameindex()

def test_if_nameindex():
    """
    Test socket.if_nameindex()
    """
    # Get the interface name and index
    if_nameindex = socket.if_nameindex()
    # Check if the interface name and index is correct
    assert if_nameindex[0] == ("lo", 1)

# Test socket.if_nametoindex()

def test_if_nametoindex():
    """
    Test socket.if_nametoindex()
    """
    # Get the interface index
    if_index = socket.if_nametoindex("lo")
    # Check
