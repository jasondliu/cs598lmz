import ctypes
import ctypes.util
import threading
import sqlite3
import time
import os
import sys

#------------------------------------------------------------------------------
#
#------------------------------------------------------------------------------

class Pcap(object):

    def __init__(self, device, filter_string, snaplen):
        self.device = device
        self.filter_string = filter_string
        self.snaplen = snaplen
        self.pcap_t = None

    def open(self):
        self.pcap_t = pcap_open_live(self.device, self.snaplen, 1, 0, self.errbuf)
        if not self.pcap_t:
            raise PcapError("pcap_open_live failed: %s" % self.errbuf)

        if self.filter_string:
            if pcap_compile(self.pcap_t, self.bpf, self.filter_string, 0, 0) == -1:
                raise PcapError("pcap_compile failed: %s" % pcap_geterr(self.pcap_t))
