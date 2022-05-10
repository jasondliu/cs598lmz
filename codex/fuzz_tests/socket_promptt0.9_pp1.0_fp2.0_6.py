import socket
# Test socket.if_indextoname
print(socket.if_indextoname(1))
for ifname in ('lo', 'eth0', 'eth1'):
    ifindex = socket.if_nametoindex(ifname)
    ifn = socket.if_indextoname(ifindex)
    assert ifn == ifname, (ifn, ifname)
    print(ifn)
