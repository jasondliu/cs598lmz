import socket
socket.if_indextoname(2)

%%python3
import socket, fcntl, struct
name = "enp0s3"
SIOCGIFINDEX = 0x8933
#sniffer = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(ETH_P_ALL))
sniffer = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(3))
index = fcntl.ioctl(sniffer.fileno(), SIOCGIFINDEX, struct.pack('256s', name.encode()))
index = struct.unpack('I', index)[0]
print(index)
socket.if_indextoname(index)

# index = 32


import socket, fcntl, struct

sniffer = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(3))
interface = socket.inet_ntoa(fcntl.ioctl(sniffer.fileno(), SIOCGIFADDR)[
