import socket
# Test socket.if_indextoname()

def if_indextoname(ifindex):
    try:
        return socket.if_indextoname(ifindex)
    except:
        return None

def if_nametoindex(ifname):
    try:
        return socket.if_nametoindex(ifname)
    except:
        return None

ifaces = if_indextoname(0)
while ifaces:
    print "interface name %s" % ifaces
    ifaces = if_indextoname(if_nametoindex(ifaces) + 1)
