import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    assert socket.if_indextoname(1) == 'lo'
    assert socket.if_indextoname(2) == 'eth0'
    assert socket.if_indextoname(3) == 'wlan0'
    assert socket.if_indextoname(4) == 'eth1'

# Test socket.if_nametoindex()

def test_if_nametoindex():
    assert socket.if_nametoindex('lo') == 1
    assert socket.if_nametoindex('eth0') == 2
    assert socket.if_nametoindex('wlan0') == 3
    assert socket.if_nametoindex('eth1') == 4

# Test socket.getifaddrs()

def test_getifaddrs():
    ifaddrs = socket.getifaddrs()
    assert len(ifaddrs) == 4
    assert ifaddrs[0].family == socket.AF_INET
    assert ifaddrs[0].netmask == socket.inet_nt
