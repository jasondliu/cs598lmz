import socket
socket.if_indextoname('5')

#%%

import os
import sys
import subprocess
import netifaces

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

def get_ip_address_ifconfig(ifname):
    #p = subprocess.Popen(["ifconfig", ifname], stdout=subprocess.PIPE)
    #return p.communicate()[0]
    return netifaces.ifaddresses(ifname)[netifaces.AF_INET][0]['addr']

def get_ip_address_socket(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
