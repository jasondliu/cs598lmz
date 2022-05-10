import _struct
import socket

# Import the pypcap module
import pcap

# Import the pypcap module
import pcap

# Open the device in promiscuous mode
p = pcap.pcapObject()
dev = pcap.lookupdev()
net, mask = pcap.lookupnet(dev)
p.open_live(dev, 1600, 0, 100)

# Start looping through packets
p.setfilter('icmp', 0, 0)

while 1:
	try: 
		p.dispatch(1, print_packet)
	except KeyboardInterrupt:
		break
