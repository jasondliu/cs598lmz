import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    ifname = socket.if_indextoname(1)
    if ifname is None:
        raise TestSkipped("this platform doesn't support interface enumeration")
    if ifname not in socket.if_nameindex():
        raise TestFailed("interface %s not found" % ifname)

test_if_indextoname()
