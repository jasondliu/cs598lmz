import _struct
import ipaddress
import random
import re
import time
import data_parser

class Network:
    def __init__(self, data, len_size):

        self.gamma = 1
        self.eps = 1

        self.mac_format = "6s"
        self.ethernet_format = "!H6s6s" + 10 * "x"
        self.enumerate = {
            "ip": 1,
            "tcp": 6,
            "udp": 17,
            "icmp": 1,
            "arp": 27,
            "arp_answ": 28
        }

        self.data = data
        self.len_size = len_size
        self.offset = 14

        self.total_packets_len = self.size_of_all_data()

        # Maps number of packet -> [packet_len, packet_type]
        self.packet_order = self.compute_packets_order()
        self.probabilities = self.calcu_prob()


