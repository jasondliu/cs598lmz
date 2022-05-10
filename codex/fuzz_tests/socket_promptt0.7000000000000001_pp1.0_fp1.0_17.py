import socket
# Test socket.if_indextoname

def test_if_indextoname(dev, apdev):
    """socket.if_indextoname"""
    ifname = socket.if_indextoname(dev[0].ifindex)
    if ifname != dev[0].ifname:
        raise Exception("Unexpected ifindex result for %s: %s" % (dev[0].ifname, ifname))
    ifname = socket.if_indextoname(dev[1].ifindex)
    if ifname != dev[1].ifname:
        raise Exception("Unexpected ifindex result for %s: %s" % (dev[1].ifname, ifname))
    ifname = socket.if_indextoname(dev[0].ifindex + 1)
    if ifname != None:
        raise Exception("Unexpected ifindex result for invalid index: %s" % ifname)

def test_if_nameindex(dev, apdev):
    """socket.if_nameindex"""
    if_nameindex = socket.if_nameindex()
    if if_nameindex[0
