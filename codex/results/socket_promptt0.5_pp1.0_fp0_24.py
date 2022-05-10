import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    """Test socket.if_indextoname()."""

    assert socket.if_indextoname(1) == 'lo'
    assert socket.if_indextoname(2) == 'eth0'
    assert socket.if_indextoname(4) == 'wlan0'
    assert socket.if_indextoname(5) == 'wlan1'
    assert socket.if_indextoname(6) == 'wlan2'
    assert socket.if_indextoname(7) == 'wlan3'
    assert socket.if_indextoname(8) == 'wlan4'
    assert socket.if_indextoname(9) == 'wlan5'
    assert socket.if_indextoname(10) == 'wlan6'
    assert socket.if_indextoname(11) == 'wlan7'
    assert socket.if_indextoname(12) == 'wlan8'
    assert socket.if_indexton
