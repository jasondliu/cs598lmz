import socket
# Test socket.if_indextoname() and socket.if_nametoindex() on FreeBSD
# and verify connectability.

hostip = socket.gethostbyaddr('localhost')[2][0]

# Create a TCP socket and bind it to a raw interface.
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((hostip, 0))

# Get an assigned index from the raw interface name.
ifname = socket.if_nameindex()[-1][1]
ifindex = socket.if_nametoindex(ifname)

# Take down the interface temporarily so that we can force a
# connect failure.
ioctl = fcntl.ioctl(sock.fileno(), SIOCIFDESTROY)
os.write(sock.fileno(), ifname + '\0' * (IFNAMSIZ - len(ifname)))

# Get the raw interface name from the index and verify it.
sname = socket.if_indextoname(ifindex)
print('ifname: %s, sname: %s' % (
