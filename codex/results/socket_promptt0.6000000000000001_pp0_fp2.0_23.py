import socket
# Test socket.if_indextoname() method

import socket
import subprocess
import sys

def if_indextoname(ifindex):
    '''Get the interface name given the interface index'''
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        ifname = socket.if_indextoname(ifindex)
        return ifname
    except IOError:
        return None

def get_ip_address(ifname):
    '''Get the IP address of the interface'''
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        ip = socket.inet_ntoa(fcntl.ioctl(s.fileno(),
                            0x8915, # SIOCGIFADDR
                            struct.pack('256s', ifname[:15])
                            )[20:24])
        return ip
    except IOError:
        return None


def main():
    '''Main method'''
    ifindex = 0
    while True:

