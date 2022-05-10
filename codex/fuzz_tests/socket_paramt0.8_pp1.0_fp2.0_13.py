import socket
socket.if_indextoname(2)

>>> 'Ethernet'

» sock = socket(...)

# Receive packets
sock.recv(bytes_to_recv)

» (data, (proto, pkttype, devname)) = sock.recv(bytes_to_recv)

# See if packet is ours
if devname == iface:

# See if packet is IPv4 or IPv6
if proto == ETH_P_IP or proto == ETH_P_IPV6:

# See if packet is broadcast or multicast
if pkttype == PACKET_BROADCAST or pkttype == PACKET_MULTICAST:

# Send packets
sock.send(pkt)

>>> sock = socket(...)

>>> pkt = ...

>>> sock.send(pkt)


len

socket.ntohs

socket.htonl

>>> import socket

>>> socket.ntohs(0x1234)

>>> socket.htonl(0x1234)

» def pack_ip_addr(ip_addr):
