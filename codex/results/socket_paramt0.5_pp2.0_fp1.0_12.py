import socket
socket.if_indextoname(socket.if_nametoindex('eth0'))

import os
import time
import socket

from scapy.all import *
from scapy.layers.inet import IP, TCP
from scapy.layers.l2 import Ether

from threading import Thread
from datetime import datetime
from collections import defaultdict


class Sniffer(Thread):
    def __init__(self):
        super(Sniffer, self).__init__()
        self.daemon = True

        self.pkts = defaultdict(list)
        self.sessions = defaultdict(list)

    def run(self):
        try:
            sniff(filter="tcp", prn=self.on_packet, store=0,
                  iface=socket.if_indextoname(socket.if_nametoindex('eth0')))
        except socket.error:
            print("Error: You need root privileges to run this script")
            exit(1)

    def on_packet(self, pkt):
        if not pkt.haslayer(IP) or
