import socket
socket.if_indextoname(4)

# The next step is to get the interface's IP address:
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# This call requests the interface's current IP address.
print 'Address:', repr(fcntl.ioctl(
    s.fileno(),
    0x8915,  # SIOCGIFADDR
    struct.pack('256s', ifname[:15])
)[20:24])

# If you also want to get the netmask, use SIOCGIFNETMASK instead.
print 'netmask:', repr(fcntl.ioctl(
    s.fileno(),
    0x891b,  # SIOCGIFNETMASK
    struct.pack('256s', ifname[:15])
)[20:24])

# If you also want to get the broadcast address, use SIOCGIFBRDADDR instead.
print 'broadcast:', repr(fcntl.ioctl(
    s.fileno(),
    0x8919,  # SIOCGIFBR
