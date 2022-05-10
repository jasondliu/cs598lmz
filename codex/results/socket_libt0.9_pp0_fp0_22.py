import socket
from tqdm import tqdm
import argparse
from argparse import RawTextHelpFormatter
from os import _exit

from netfilterqueue import NetfilterQueue # debian package: python3-nfqueue
from scapy.all import * # debian package: python3-scapy
from scapy.layers.http import HTTPRequest # requires scapy > 2.4.0 or patched Scapy
from scapy.layers.inet import IP, UDP, ICMP
from scapy.layers.dns import DNS, DNSRR, DNSQR

nfqueue = NetfilterQueue()

class UpdateDNSRR(Packet):
    name = "ADD_DNSRR"
    fields_desc = [ ShortEnumField("type", 1, DNSRRtypes),
                    ShortField("rr_class", 1),
                    IntField("ttl", 0),
                    FieldLenField("rdlen", None, length_of="rdata", fmt="!H"),
                    RDATAField("rdata", "", length_from=lambda pkt:pkt.rdlen) ]
    def extract_padding
