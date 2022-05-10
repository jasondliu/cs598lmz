import socket
# Test socket.if_indextoname
def test_if_indextoname():
    assert socket.if_indextoname(1) == 'lo'

# Test socket.if_indextoname
def test_if_nameindex():
    assert socket.if_nameindex() == [(1, 'lo')]

# Test socket.if_nametoindex
def test_if_nametoindex():
    assert socket.if_nametoindex('lo') == 1

# Test socket.if_nameindex
def test_if_nameindex():
    assert socket.if_nameindex() == [(1, 'lo')]
