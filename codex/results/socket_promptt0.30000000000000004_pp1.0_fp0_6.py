import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    ifname = socket.if_indextoname(1)
    if ifname is not None:
        print "Interface 1:", ifname

test_if_indextoname()
