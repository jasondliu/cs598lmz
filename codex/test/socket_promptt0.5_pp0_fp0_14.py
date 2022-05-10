import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    assert socket.if_indextoname(1) == 'lo'
    assert socket.if_indextoname(2) == 'eth0'

# Test socket.if_nametoindex()

def test_if_nametoindex():
    assert socket.if_nametoindex('lo') == 1
    assert socket.if_nametoindex('eth0') == 2
