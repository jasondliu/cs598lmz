import socket
import struct

from netaddr import IPNetwork
from netaddr import IPAddress
from struct import *

# Binarize String to IPV4
def binarize_strings_to_ipv4(ipv4_string):
    return int(str(IPAddress(ipv4_string)))

# Binarize String to IPV4
def binarize_ipv4_to_strings(ipv4):
    return str(IPNetwork(ipv4))[:-3]

class CMPUtils():

    # Frame EtherType
    FRAME_ETHERTYPE_IP = 0x0800
    FRAME_ETHERTYPE_ARP = 0x0806

    # IP Protocol
    IP_PROTOCOL_ICMP = 1
    IP_PROTOCOL_TCP = 6
    IP_PROTOCOL_UDP = 17

    # Source/Destination Mac */
    FRAME_DESTINATION_MAC = '\xff\xff\xff\xff\xff\xff'
    FRAME_SOURCE_MAC = '\x00\x00
