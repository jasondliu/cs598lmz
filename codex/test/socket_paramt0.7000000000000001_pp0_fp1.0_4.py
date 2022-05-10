import socket
socket.if_indextoname("3")

#!/usr/bin/env python
from scapy.all import *
import time

local_mac = 'xx:xx:xx:xx:xx:xx'
local_ip = '192.168.1.1'

def arp_display(pkt):
  if pkt[ARP].op == 1: #who-has (request)
    if pkt[ARP].psrc == '0.0.0.0': # ARP Probe
      if pkt[ARP].hwsrc == 'xx:xx:xx:xx:xx:xx': # Airpods
        time.sleep(1)
