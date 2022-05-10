import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    if_indextoname = socket.if_indextoname
    if_indextoname(1)
    if_indextoname(1, 'lo')
    if_indextoname(1, 'lo', 'eth0')
    if_indextoname(1, 'lo', 'eth0', 'wlan0')
    if_indextoname(1, 'lo', 'eth0', 'wlan0', 'wlan1')
    if_indextoname(1, 'lo', 'eth0', 'wlan0', 'wlan1', 'wlan2')
    if_indextoname(1, 'lo', 'eth0', 'wlan0', 'wlan1', 'wlan2', 'wlan3')
    if_indextoname(1, 'lo', 'eth0', 'wlan0', 'wlan1', 'wlan2', 'wlan3', 'wlan4')
    if_indextoname(1, 'lo', 'eth0
