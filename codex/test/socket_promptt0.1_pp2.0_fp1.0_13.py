import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    assert socket.if_indextoname(1) == 'lo'
    assert socket.if_indextoname(2) == 'eth0'
    assert socket.if_indextoname(3) == 'wlan0'
    assert socket.if_indextoname(4) == 'ppp0'
    assert socket.if_indextoname(5) == 'tun0'
    assert socket.if_indextoname(6) == 'sit0'
    assert socket.if_indextoname(7) == 'ip6tnl0'
    assert socket.if_indextoname(8) == 'eth1'
    assert socket.if_indextoname(9) == 'wlan1'
    assert socket.if_indextoname(10) == 'ppp1'
    assert socket.if_indextoname(11) == 'tun1'
    assert socket.if_indextoname(12) == 'sit1'
    assert socket.if_ind
