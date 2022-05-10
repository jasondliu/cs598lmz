import socket
import time
import threading
import struct
import sys
import os
import traceback

import utils

#
# Packet format:
#   Header:
#     0: command byte
#     1: sequence number
#     2: packet length (not including header)
#     3: checksum
#   Data:
#     4: data
#

class PacketHeader(object):
    command = 0
    seq_no = 0
    length = 0
    checksum = 0

class Packet(object):
    header = PacketHeader()
    data = ''

class PacketManager(object):
    def __init__(self, packet_size=1024, max_packets=10):
        self.packet_size = packet_size
        self.max_packets = max_packets
        self.lock = threading.Lock()
        self.packets = []
        self.seq_no = 0

    def add_packet(self, packet):
        self.lock.acquire()
