import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    # Test if_indextoname()
    ifname = socket.if_indextoname(1)
    assert ifname == 'lo'
    ifname = socket.if_indextoname(2)
    assert ifname == 'eth0'
    ifname = socket.if_indextoname(3)
    assert ifname == 'wlan0'
    ifname = socket.if_indextoname(4)
    assert ifname == 'wlan1'
    ifname = socket.if_indextoname(5)
    assert ifname == 'wlan2'
    ifname = socket.if_indextoname(6)
    assert ifname == 'wlan3'
    ifname = socket.if_indextoname(7)
    assert ifname == 'wlan4'
    ifname = socket.if_indextoname(8)
    assert ifname == 'wlan5'
    ifname = socket.if_indextoname(9)
   
