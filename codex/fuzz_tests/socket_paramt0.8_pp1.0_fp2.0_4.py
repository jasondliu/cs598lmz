import socket
socket.if_indextoname(0)
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
s.bind(("", 80))
s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

import scapy.all as scapy

# Source IP, Source Port, Destination IP, Destination Port

scapy.IP(src='10.0.2.4', dst='10.0.2.5')/scapy.TCP(sport=80, dport=80)



data = s.recv(65535)
