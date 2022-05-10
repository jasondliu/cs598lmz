import socket
# Test socket.if_indextoname()
import random
import struct

# Try to use the real interface name
try:
    if_name = socket.if_indextoname(1)
except OSError:
    # Fallback to a random name if fake interface name is not available
    if_name = 'lo' + str(random.randrange(10**4, 10**5))

# Construct the payload for a packet
pkt = IP(src='192.168.1.10', dst='192.168.1.11') / ICMP() / Raw(load='apple')

# Send the packet
send(pkt, iface=if_name)

#===============================================
# create_icmp_packet()
#
# Create a packet and return the packet object
#
# Parameters:
#    none
#
# Return:
#    pkt: packet object
#===============================================
def create_icmp_packet():
    pkt = IP(src='192.168.1.10', dst='192.168.1.11') / ICMP() / Raw(load='apple')
