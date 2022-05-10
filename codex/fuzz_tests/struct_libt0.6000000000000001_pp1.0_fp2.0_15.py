import _struct
import socket
import fcntl
import array
import time
import random

class GetHostIP(object):
    def __init__(self):
        self.__ip_list = []

    def __get_ip_list(self):
        interfaces = ['eth0', 'eth1', 'eth2', 'wlan0', 'wlan1', 'wifi0', 'ath0', 'ath1', 'ppp0']
        max_possible = 128  # arbitrary. raise if needed.
        bytes = max_possible * 32
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        names = array.array('B', '\0' * bytes)
        outbytes = struct.unpack('iL', fcntl.ioctl(
            s.fileno(),
            0x8912,  # SIOCGIFCONF
            struct.pack('iL', bytes, names.buffer_info()[0])
        ))[0]
        namestr = names.tostring()
        for i
