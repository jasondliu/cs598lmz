import socket
socket.if_indextoname(3)

import netifaces
netifaces.interfaces()
netifaces.ifaddresses('eth0')
netifaces.ifaddresses('eth0')[netifaces.AF_LINK]
netifaces.ifaddresses('eth0')[netifaces.AF_LINK][0]['addr']
netifaces.ifaddresses('eth0')[netifaces.AF_INET]
netifaces.ifaddresses('eth0')[netifaces.AF_INET][0]['addr']

import re
import netifaces

def get_ip_address(ifname):
    if netifaces.AF_INET in netifaces.ifaddresses(ifname):
        return netifaces.ifaddresses(ifname)[netifaces.AF_INET][0]['addr']
    else:
        return None

