import socket
socket.if_indextoname(1)

# SIOCGIFHWADDR
socket.ioctl(s, 0x8927, 'lo')

# SIOCGIFADDR
socket.ioctl(s, 0x8915, b'lo')

# SIOCGIFMTU
socket.ioctl(s, 0x8921, 'lo')

# SIOCGIFNAME
socket.ioctl(s, 0x8910, struct.pack("L", 2))


# SIOCGIFCONF
c = b'\0' * 16 * 8
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket.ioctl(s, 0x8912, struct.pack('iL', 16 * 8, c))
print(struct.unpack('iL', struct.unpack(str(16 * 8) + 's', c)[0]))

# SIOCGIFFLAGS
socket.ioctl(s, 0x8913, 'lo')

# SIOCGIFPFLAGS
# socket.ioctl(s, 0
