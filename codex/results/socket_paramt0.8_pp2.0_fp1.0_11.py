import socket
socket.if_indextoname(1)

s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
s.bind(("192.168.0.105",0))
s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

for i in range(0,200):
    packet = s.recvfrom(65565)
    try:
        eth_len=14
        eth_header = packet[0][0:eth_len]
        eth = unpack('!6s6sH' , eth_header)
        eth_protocol = socket.ntohs(eth[2])
        print "Protocol: " + str(eth_protocol)
        print "Dest MAC: " + ':'.join(x.encode('hex') for x in packet[0][0:6]) + ' Source MAC: ' + ':'.join(x.encode('hex') for x in
