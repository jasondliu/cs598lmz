import socket
socket.if_indextoname(0)

#Open pcap file
f = open ("/home/manoj/Downloads/in.pcap", "rb")
pcap = dpkt.pcap.Reader(f)

#read all the packets in the pcap file
for ts, buf in pcap:
    ethernet = dpkt.ethernet.Ethernet(buf) #unpack the buffer

    #skip packets that are not IP
    if not isinstance(ethernet.data, dpkt.ip.IP):
        continue;

    ip = ethernet.data #unpack the ip packet

    #skip packets that are not TCP
    if not isinstance(ip.data, dpkt.tcp.TCP):
        continue;

    tcp = ip.data #unpack the tcp packet

    if len(tcp.data) == 0 or tcp.dport != 80: #skip non-http packets and non-data packets
        continue

