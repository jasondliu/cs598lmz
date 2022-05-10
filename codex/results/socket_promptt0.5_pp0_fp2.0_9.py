import socket
# Test socket.if_indextoname()
for i in range(256):
    try:
        print('{}: {}'.format(i, socket.if_indextoname(i)))
    except OSError:
        pass

# Test socket.if_nametoindex()
for i in range(256):
    ifname = socket.if_indextoname(i)
    if ifname:
        print('{}: {}'.format(ifname, socket.if_nametoindex(ifname)))

# Test socket.if_nameindex()
print('\n'.join(['{}: {}'.format(ifname, ifindex) for ifindex, ifname in socket.if_nameindex()]))

# Test socket.if_nametoindex()
print('\n'.join(['{}: {}'.format(ifname, socket.if_nametoindex(ifname)) for ifindex, ifname in socket.if_nameindex()]))

# Test socket.if_indextoname()
print('\n'.join(['{}: {}'.format(ifindex, socket.if_indext
