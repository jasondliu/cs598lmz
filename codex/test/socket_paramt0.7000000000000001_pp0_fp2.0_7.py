import socket
socket.if_indextoname('0')

# To get the interface name from a value, use the ioctl() function with the
# interface control request SIOCGIFNAME. For example:
#
# >>> import fcntl
# >>> socket.if_indextoname(0)
# 'lo'
# >>> fcntl.ioctl(s.fileno(), 0x8915, b'\x00\x00\x00\x00')
# b'lo'
