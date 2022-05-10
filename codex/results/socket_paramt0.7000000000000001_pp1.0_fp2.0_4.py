import socket
socket.if_indextoname(socket.if_nametoindex('en0'))

# Get the first IP address for the given network interface
socket.if_indextoname(socket.if_nametoindex('en0')), socket.inet_ntoa(fcntl.ioctl(
    s.fileno(),
    0x8915,  # SIOCGIFADDR
    struct.pack('256s', ifname[:15])
)[20:24])

# Get the MAC address for the given network interface
socket.if_indextoname(socket.if_nametoindex('en0')), ''.join(['%02x:' % ord(char) for char in fcntl.ioctl(
    s.fileno(),
    0x8927,  # SIOCGIFHWADDR
    struct.pack('256s', ifname[:15])
)[18:24]])[:-1]

# Get the broadcast address for the given network interface
socket.if_indextoname(socket.if_nametoindex('en0')), socket.inet_ntoa(fcnt
