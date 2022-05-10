import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    # Test if_indextoname()
    ifname = socket.if_indextoname(1)
    assert ifname == 'lo'
    assert socket.if_indextoname(1, 'lo') == 'lo'
    assert socket.if_indextoname(1, 'eth0') == 'lo'
    assert socket.if_indextoname(1, 'eth1') == 'lo'
    assert socket.if_indextoname(1, 'eth2') == 'lo'
    assert socket.if_indextoname(1, 'eth3') == 'lo'
    assert socket.if_indextoname(1, 'eth4') == 'lo'
    assert socket.if_indextoname(1, 'eth5') == 'lo'
    assert socket.if_indextoname(1, 'eth6') == 'lo'
    assert socket.if_indextoname(1, 'eth7') == 'lo'
    assert socket.if_indext
