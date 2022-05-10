import socket
# Test socket.if_indextoname

# Create a socket to query the interface index
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Get the interface index
ifindex = s.getsockopt(socket.SOL_SOCKET, socket.SO_IFINDEX)

# Get the interface name
ifname = socket.if_indextoname(ifindex)

# Check that the name is correct
if ifname != 'lo0':
    print('FAIL: if_indextoname returned %s instead of "lo0"' % ifname)
else:
    print('PASS: if_indextoname returned "lo0"')
