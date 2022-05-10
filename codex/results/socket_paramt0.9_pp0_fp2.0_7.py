import socket
socket.if_indextoname(65027)
'en0' # the WiFi interface

interface_name = 'en0'

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0x8915,  # SIOCGIFADDR
                                struct.pack('256s', bytes(ifname[:15], 'utf-8')))[20:24])

ip = get_ip_address(interface_name)
print(ip)

# PART 2:

from mac_vendor_lookup import MacLookup

mac_lookup = MacLookup()

from scapy.all import *
conf.verb = 0

from mac_vendor_lookup import MacLookup

import time
from datetime import datetime
from scapy.all import *


interface_name = "en0"
macLookup = MacLookup()

# Create a new ARP request
def arp_display(
