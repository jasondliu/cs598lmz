import socket
# Test socket.if_indextoname.
# This test is only valid on Linux.

def test_if_indextoname(dev, apdev):
    """socket.if_indextoname"""
    ifname = socket.if_indextoname(1)
    if ifname is None:
        raise HwsimSkip('socket.if_indextoname is not supported')
    if "mon." + dev[0] not in ifname:
        raise Exception("Unexpected ifname: " + ifname)

def test_if_indextoname_invalid(dev, apdev):
    """socket.if_indextoname with invalid index"""
    ifname = socket.if_indextoname(0)
    if ifname is not None:
        raise Exception("Unexpected ifname: " + ifname)

def test_if_indextoname_invalid2(dev, apdev):
    """socket.if_indextoname with invalid index"""
    ifname = socket.if_indextoname(10000)
    if ifname is not None:
        raise Exception
