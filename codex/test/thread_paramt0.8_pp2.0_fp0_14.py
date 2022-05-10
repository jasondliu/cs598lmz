import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello World\n')).start()
threading.Thread(target=lambda: sys.stdout.write('Goodbye World\n')).start()

from time import sleep
from threading import Thread
from math import factorial
from collections import Counter
from itertools import repeat

from scapy.all import *

from scapy.layers.http import HTTPRequest

from netaddr import *
from netaddr.core import *
from netaddr.ip import *

from scapy.contrib.mqtt import *


# snort
# ETHERNET
# IP, IPv6
# TCP
# UDP
# ICMP
# GRE
# ARP
# SCTP
# DNS
# DHCP
# BOOTP
# HTTP
# MQTT


def pkt_callback(pkt):
    pkt.show()


def map_snort_2_scapy(p):
    """
    :param p:
    :return:
    """
    p.show()
    p_ether = Ether(p[0])
