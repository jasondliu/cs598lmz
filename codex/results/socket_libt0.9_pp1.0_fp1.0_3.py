import socket
import struct
from struct import unpack
from struct import pack
from ctypes import *
from collections import namedtuple

from Config import *
#import cpp_wrappers.cpp_substrate as cpp_substrate
from Util import pypcap, is_debug
import Log


class Csock(socket.socket):
    send_lock = threading.RLock()

    def __init__(self):
        socket.socket.__init__(self, socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
        self.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

    def sr(self, ip_obj, tcp_obj):
        dest_ip_raw = socket.inet_aton(ip_obj.dst)
        ip_header = self.pack_ip_header(ip_obj)
        tcp_header = self.pack_tcp_header(tcp_obj)
        packet = ip_header + tcp_header
        try:
            self.sendto
