import socket
import struct
import sys
import time
import subprocess

from scapy.config import conf
from scapy.fields import *
from scapy.packet import *
from scapy.layers.inet import *
from scapy.sendrecv import sr1 
from scapy.supersocket import StreamSocket

import scapy_http.http

class Packet(Packet):
    name = "Packet"
    fields_desc = [
        ByteField("nf_magic", 0xAA),
        ByteField("nf_ver", 0x01),
        ByteField("nf_res", 0x00),
        ByteField("nf_type", 0x01),
        IntField("nf_len", None),
    ]

    def post_build(self, pkt, pay):
        pkt = pkt[:4] + struct.pack("!I", len(pkt) + len(pay)) + pkt[8:]
        return pkt + pay

class Packet_payload(Packet):
    name = "Packet_payload
