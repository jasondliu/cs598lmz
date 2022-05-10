import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    assert socket.if_indextoname(1) == 'lo'
    assert socket.if_indextoname(2) == 'eth0'
    assert socket.if_indextoname(3) == 'wlan0'
    assert socket.if_indextoname(4) == 'eth1'
    assert socket.if_indextoname(5) == 'wlan1'
    assert socket.if_indextoname(6) == 'eth2'
    assert socket.if_indextoname(7) == 'wlan2'
    assert socket.if_indextoname(8) == 'eth3'
    assert socket.if_indextoname(9) == 'wlan3'
    assert socket.if_indextoname(10) == 'eth4'
    assert socket.if_indextoname(11) == 'wlan4'
    assert socket.if_indextoname(12) == 'eth5'
    assert socket.if_indexton
