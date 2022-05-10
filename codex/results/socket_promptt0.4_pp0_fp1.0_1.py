import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    ifname = socket.if_indextoname(1)
    if ifname != 'lo':
        raise TestFailed, "if_indextoname(1) should return 'lo', not %s" % ifname
    if socket.if_indextoname(1) != 'lo':
        raise TestFailed, "if_indextoname(1) should return 'lo'"
    if socket.if_indextoname(2) != 'eth0':
        raise TestFailed, "if_indextoname(2) should return 'eth0'"
    if socket.if_indextoname(3) != 'sit0':
        raise TestFailed, "if_indextoname(3) should return 'sit0'"
    if socket.if_indextoname(4) != 'lo':
        raise TestFailed, "if_indextoname(4) should return 'lo'"
    if socket.if_indextoname(5) != 'eth1':
        raise TestF
