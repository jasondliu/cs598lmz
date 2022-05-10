import socket
import struct
import sys

from scapy.all import *

def main():
    if len(sys.argv) != 2:
        print "Usage: python %s <iface>" % sys.argv[0]
        sys.exit(1)

    iface = sys.argv[1]

    pkt = Ether(src=get_if_hwaddr(iface), dst='ff:ff:ff:ff:ff:ff') / \
        ARP(op=ARP.who_has, psrc='0.0.0.0', pdst='192.168.1.1')

    print "Sending ARP who-has request for 192.168.1.1 on %s" % iface
    sendp(pkt, iface=iface)

    sniff(iface=iface, filter="arp and arp[7] = 2", prn=arp_display, store=0)


def arp_display(pkt):
    if pkt[ARP].op == 2:
        print "ARP Reply: %s is at %s
