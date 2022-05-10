import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    ifname = socket.if_indextoname(1)
    if ifname is None:
        raise TestFailed, "if_indextoname(1) returned None"
    if ifname not in socket.if_nameindex():
        raise TestFailed, "if_indextoname(1) returned an unknown interface name"

test_if_indextoname()
