import socket
socket.if_indextoname(3)

#pip install netifaces

import netifaces
netifaces.interfaces()

netifaces.ifaddresses('eth0')

netifaces.ifaddresses('eth0')[netifaces.AF_INET][0]['addr']

#pip install netaddr

from netaddr import *

ip = IPNetwork('192.168.1.0/24')
ip.netmask
ip.broadcast
ip.size
ip.first
ip.last

ip.iter_hosts()

