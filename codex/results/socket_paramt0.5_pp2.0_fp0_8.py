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

for host in ip.iter_hosts():
    print host
    
#pip install python-nmap

import nmap

nm = nmap.PortScanner()
nm.scan('192.168.1.0/24', '22-443')

nm.command_line()
nm.scaninfo()
nm.all_hosts()
nm['127.0.0.1'].hostname()
nm['127.0.0.1'].state()
nm['127.0.0.1'].
