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
        print "ARP Probe from: " + pkt[ARP].hwsrc
        send(ARP(op=2, pdst=local_ip, psrc=local_ip, hwdst=pkt[ARP].hwsrc)) # Airpods

print sniff(prn=arp_display, filter="arp", store=0, count=0)

#!/usr/bin/env python
from scapy.all import *
import time
import socket

local
