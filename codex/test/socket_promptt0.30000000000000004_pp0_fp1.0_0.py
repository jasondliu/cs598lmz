import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    # Test if_indextoname()
    ifname = socket.if_indextoname(1)
    assert ifname == 'lo'

def test_if_nameindex():
    # Test if_nameindex()
    ifnames = socket.if_nameindex()
    assert ifnames[0] == (1, 'lo')

def test_if_nametoindex():
    # Test if_nametoindex()
    ifindex = socket.if_nametoindex('lo')
    assert ifindex == 1
