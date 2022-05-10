import socket
import sys
import time
import threading
import random
import os

from scapy.all import *

from . import utils
from . import config
from . import logger

class Sniffer(threading.Thread):
    def __init__(self, interface, output_file):
        threading.Thread.__init__(self)
        self.interface = interface
        self.output_file = output_file
        self.stop_sniffer = threading.Event()

    def run(self):
        sniff(iface=self.interface, prn=self.process_packet, store=0)

    def process_packet(self, packet):
        if packet.haslayer(Dot11):
            if packet.type == 0 and packet.subtype == 8:
                utils.write_packet(self.output_file, packet)
                logger.info("[+] Packet captured")

    def stop(self):
        self.stop_sniffer.set()

