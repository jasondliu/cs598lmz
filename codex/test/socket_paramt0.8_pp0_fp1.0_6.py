import socket
socket.if_indextoname('5')

# ipconfig /all -> find name associated with the interface index

# 2. Sending ARP request with custom source mac address

import socket
import struct

# create socket
sock = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(3))
sock.bind(("Intel(R) Dual Band Wireless-AC 8260", socket.htons(0x0800)))

# raw socket -> receives with payload
# handcrafted

# ARP packet in binary
# https://tools.ietf.org/html/rfc826
# https://en.wikipedia.org/wiki/Address_Resolution_Protocol
# https://github.com/OpenSecurityResearch/packet-classifier/blob/master/arp.py
# https://github.com/OpenSecurityResearch/packet-classifier/blob/master/constant.py

# destination MAC 00:00:00:00:00:00
# 802.1Q ethernet frame
# destination MAC 00:00:00:00:00:00

#
