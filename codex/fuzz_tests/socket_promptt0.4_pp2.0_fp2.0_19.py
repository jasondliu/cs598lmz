import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    ifname = socket.if_indextoname(1)
    assert ifname == 'lo'

def test_if_nameindex():
    ifname = socket.if_nameindex()
    assert ifname[0] == (1, 'lo')
