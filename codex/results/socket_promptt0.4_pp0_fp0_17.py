import socket
# Test socket.if_indextoname()

def test_if_indextoname(dev, ifname):
    try:
        devname = socket.if_indextoname(dev)
    except:
        print "socket.if_indextoname() not supported"
        return

    if devname != ifname:
        print "socket.if_indextoname() failed"
        print "Expected:", ifname
        print "Got:", devname

# Test socket.if_nametoindex()

def test_if_nametoindex(dev, ifname):
    try:
        devnum = socket.if_nametoindex(ifname)
    except:
        print "socket.if_nametoindex() not supported"
        return

    if devnum != dev:
        print "socket.if_nametoindex() failed"
        print "Expected:", dev
        print "Got:", devnum

# Test socket.if_nameindex()

def test_if_nameindex():
    try:
        iflist = socket.if_nameindex()
    except:
