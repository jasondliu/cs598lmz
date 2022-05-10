import socket
# Test socket.if_indextoname()

def test_if_indextoname(dev, funcname):
    ifname = socket.if_indextoname(dev)
    if ifname is None:
        print "socket.%s(%d): %s" % (funcname, dev, ifname)
    else:
        print "socket.%s(%d): %s" % (funcname, dev, ifname)

# Test socket.if_nameindex()

def test_if_nameindex(funcname):
    iflist = socket.if_nameindex()
    print "socket.%s(): %s" % (funcname, iflist)

# Test socket.if_nametoindex()

def test_if_nametoindex(ifname, funcname):
    ifindex = socket.if_nametoindex(ifname)
    if ifindex is None:
        print "socket.%s(%s): %s" % (funcname, ifname, ifindex)
    else:
        print "socket.%s(%s): %s" % (funcname,
