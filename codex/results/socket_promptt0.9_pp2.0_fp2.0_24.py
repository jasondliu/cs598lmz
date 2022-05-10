import socket
# Test socket.if_indextoname() and socket.if_nametoindex()
print socket.if_nametoindex('eth0')
print socket.if_indextoname(2)
print socket.AF_INET
print socket.SOCK_STREAM

import dpkt
import binascii

eth = dpkt.ethernet.Ethernet(binascii.unhexlify(b'c7501830002831d9e38e000000000000000005704b065d5a128008000000'))
print eth

f = open('test.pcap', 'rb')
pcap = dpkt.pcap.Reader(f)

for timestamp, buf in pcap:
    eth = dpkt.ethernet.Ethernet(buf)
    if not isinstance(eth.data, dpkt.ip.IP):
        print 'Non IP Packet type not supported %s\n' % eth.data.__class__.__name__
        continue
    
    ip = eth.data

    # Pull out src, dst, length of the ip packet
