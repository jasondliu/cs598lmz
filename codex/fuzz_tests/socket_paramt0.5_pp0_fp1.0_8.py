import socket
socket.if_indextoname(socket.if_nametoindex('lo'))

# Importing pcapy library
import pcapy

# Creating a packet capture object
# dev = "lo"
dev = "eth0"
pcap = pcapy.open_live(dev, 65536, 1, 0)

# Start sniffing packets
pcap.loop(0, print_packet)
