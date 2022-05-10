import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)


# import socket
# import struct
# import binascii
#
# raw = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))
# print(raw)
# pkt = raw.recvfrom(2048)
# print(pkt)
# ethernet_header = pkt[0][0:14]
# ethernet_detailed = struct.unpack('!6s6s2s', ethernet_header)
# arp_header = pkt[0][14:42]
# arp_detailed = struct.unpack('2s2s1s1s2s6s4s6s4s', arp_header)
# # display mac get
# ethernet_list = []
# for item in ethernet_detailed:
#     ethernet_list.append(binascii.hexlify(item))
# print('Destination MAC : ' + ethernet_list[0].decode())
# print('Source MAC : ' + ethernet
