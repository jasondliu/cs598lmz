import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    # Get interface name from index
    if_index = socket.if_nametoindex('lo')
    assert socket.if_indextoname(if_index) == 'lo'

    # Get interface name from invalid index
    raises(ValueError, socket.if_indextoname, -1)

# Test socket.if_nameindex()

def test_if_nameindex():
    # Get interface index and name
    if_nameindex = socket.if_nameindex()
    if_nameindex_dict = dict(if_nameindex)
    if_index = socket.if_nametoindex('lo')
    assert if_index in if_nameindex_dict
    assert if_nameindex_dict[if_index] == 'lo'

# Test socket.if_nametoindex()

def test_if_nametoindex():
    # Get interface index from name
    assert socket.if_nametoindex('lo') > 0

    # Get interface index from invalid name
