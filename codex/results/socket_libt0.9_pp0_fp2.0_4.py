import socket
import re
import random
import string
import json

from threading import *
from time import ctime
from time import sleep
from threading import Thread
from scapy.all import *
from scapy.layers.inet import *
from scapy.layers.l2 import *

from pprint import pprint


class TCP_listener(object):
    def __init__(self):
        self.ip_list  = []
        self.mac_list = []
        self.port_list = [80, 8080, 443]
        self.dport   = random.choice(self.port_list)
        self.sport   = random.choice(self.port_list)
        self.pkt     = Ether(src=get_if_hwaddr("wlan0"), dst="ff:ff:ff:ff:ff:ff")/IP(dst="192.168.0.0/16", id=RandShort())/TCP(sport=self.sport, dport=self.dport, seq=12345, ack=1000, window=
