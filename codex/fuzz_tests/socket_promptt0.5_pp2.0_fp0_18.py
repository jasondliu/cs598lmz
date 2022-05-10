import socket
# Test socket.if_indextoname()

def test_if_indextoname(dev, funcname):
    ifindex = getattr(socket, funcname)(dev)
    name = socket.if_indextoname(ifindex)
    if name != dev:
        raise Exception("if_indextoname(%s) returned %s" % (ifindex, name))

test_if_indextoname('lo', 'if_nametoindex')
test_if_indextoname('eth0', 'if_nametoindex')
test_if_indextoname('eth1', 'if_nametoindex')
test_if_indextoname('wlan0', 'if_nametoindex')
