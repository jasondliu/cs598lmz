import socket
# Test socket.if_indextoname()

def test_if_indextoname(dev, funcname):
    ifname = socket.if_indextoname(dev)
