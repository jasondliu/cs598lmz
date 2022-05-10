import socket
socket.if_indextoname(4)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('', 0))
s.setsockopt(socket.SOL_SOCKET, socket.SO_BINDTODEVICE, b'eth0')
s.connect(('10.255.255.255', 1))
print(s.getsockname()[0])
s.close()

# import socket
# import struct
# import fcntl
#
# def get_ip_address(ifname):
#     s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     return socket.inet_ntoa(fcntl.ioctl(
#         s.fileno(),
#         0x8915,  # SIOCGIFADDR
#         struct.pack('256s', ifname[:15])
#     )[20:24])
#
# print get_ip_address('eth0')  # '192.168.0.110'
