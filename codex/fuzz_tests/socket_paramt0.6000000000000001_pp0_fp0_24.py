import socket
socket.if_indextoname(0)
socket.if_indextoname(1)

#from scapy.all import *
#pkts=rdpcap('/home/anushree/Desktop/pcap_files/port_scan.pcap')
#for pkt in pkts:
#	if pkt.haslayer(TCP) and pkt.haslayer(IP):
#		print pkt.getlayer(TCP).sport
#		print pkt.getlayer(TCP).dport
#		print pkt.getlayer(IP).src
#		print pkt.getlayer(IP).dst
#		print pkt.getlayer(TCP).seq
#		print pkt.getlayer(TCP).ack
#		print pkt.getlayer(TCP).flags
#		print pkt.time

#from scapy.all import *
#pkts=rdpcap('/home/anushree/Desktop/pcap_files/port_scan.pcap')
#for pkt in pkts:
#
