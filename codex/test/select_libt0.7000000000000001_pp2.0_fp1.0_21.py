import select
import socket
import struct
import sys

import pypacker
from pypacker.layer12 import ethernet
from pypacker.layer3 import ip
from pypacker.layer4 import udp

import ipaddress

from pypacker import ppcap
from pypacker.layer12 import ethernet
from pypacker.layer3 import ip, arp
from pypacker.layer4 import udp, tcp
from pypacker.layer567 import dns, dnsapp

# TODO: add description

# EtherType: https://en.wikipedia.org/wiki/EtherType
iface_pcap = "tun0"
bfilter = "(udp and port 53) or (ether src de:ad:be:ef:00:00) or (ether dst de:ad:be:ef:00:00)"

# start sniffing
sniffer = ppcap.Reader(iface_pcap, bpf_filter=bfilter)

# get packets
