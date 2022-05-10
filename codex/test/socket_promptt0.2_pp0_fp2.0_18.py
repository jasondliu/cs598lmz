import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    """
    Test if_indextoname()
    """
    # Test if_indextoname()
    if_indextoname = socket.if_indextoname
    assert if_indextoname(1) == 'lo'
    assert if_indextoname(2) == 'eth0'
    assert if_indextoname(3) == 'wlan0'
    assert if_indextoname(4) == 'wlan1'
    assert if_indextoname(5) == 'wlan2'
    assert if_indextoname(6) == 'wlan3'
    assert if_indextoname(7) == 'wlan4'
    assert if_indextoname(8) == 'wlan5'
    assert if_indextoname(9) == 'wlan6'
    assert if_indextoname(10) == 'wlan7'
    assert if_indextoname(11) == 'wlan8'
