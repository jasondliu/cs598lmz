import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    # Test if_indextoname()
    ifname = socket.if_indextoname(1)
    if ifname:
        print("if_indextoname(1) = %s" % ifname)
    else:
        print("if_indextoname(1) failed")

def test_if_nameindex():
    # Test if_nameindex()
    iflist = socket.if_nameindex()
    if iflist:
        print("if_nameindex() = %s" % iflist)
    else:
        print("if_nameindex() failed")

def test_if_nametoindex():
    # Test if_nametoindex()
    ifindex = socket.if_nametoindex("lo")
    if ifindex:
        print("if_nametoindex(lo) = %s" % ifindex)
    else:
        print("if_nametoindex(lo) failed")

