import socket
# Test socket.if_indextoname()
ifname = socket.if_indextoname(1) or "lo"
if ifname:
    print("success: if_indextoname(1) -> %s" % ifname)
else:
    print("failure: if_indextoname(1)")

# Test socket.if_nametoindex()
ifindex = socket.if_nametoindex(ifname)
if ifindex:
    print("success: if_nametoindex(%s) -> %s" % (ifname, ifindex))
else:
    print("failure: if_nametoindex(%s)" % ifname)

# Test socket.if_nameindex()
ifnameindex = socket.if_nameindex()
if ifnameindex:
    print("success: if_nameindex() -> %s" % ifnameindex)
else:
    print("failure: if_nameindex()")
