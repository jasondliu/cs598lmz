import socket
# Test socket.if_indextoname()
for ifindex in range(1, 10):
    try:
        ifname = socket.if_indextoname(ifindex)
        print('%d %s' % (ifindex, ifname))
    except OSError as err:
        print('%d %s' % (ifindex, err))
