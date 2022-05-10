import socket
# Test socket.if_indextoname()
def test_if_indextoname():
    assert socket.if_indextoname(0x10000000) == 'eth0'
    assert socket.if_indextoname(0x10000001) == 'eth1'
