import socket
socket.if_indextoname(3)

bcast_ip = socket.inet_ntoa(fcntl.ioctl(
    s.fileno(),
    0x8919,  # SIOCGIFBRDADDR
    struct.pack('256s', ifname[:15])
)[20:24])

