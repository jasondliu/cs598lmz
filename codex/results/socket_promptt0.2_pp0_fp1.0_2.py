import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    assert socket.if_indextoname(1) == 'lo'
    assert socket.if_indextoname(2) == 'eth0'
    assert socket.if_indextoname(3) == 'eth1'
    assert socket.if_indextoname(4) == 'eth2'
    assert socket.if_indextoname(5) == 'eth3'
    assert socket.if_indextoname(6) == 'eth4'
    assert socket.if_indextoname(7) == 'eth5'
    assert socket.if_indextoname(8) == 'eth6'
    assert socket.if_indextoname(9) == 'eth7'
    assert socket.if_indextoname(10) == 'eth8'
    assert socket.if_indextoname(11) == 'eth9'
    assert socket.if_indextoname(12) == 'eth10'
    assert socket.if_indextoname(13) ==
