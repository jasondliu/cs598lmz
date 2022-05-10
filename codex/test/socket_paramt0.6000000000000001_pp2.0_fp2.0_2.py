import socket
socket.if_indextoname(2)

import netifaces
netifaces.interfaces()
netifaces.ifaddresses('eth0')
netifaces.ifaddresses('lo')

netifaces.ifaddresses('lo')[netifaces.AF_INET]
netifaces.ifaddresses('eth0')[netifaces.AF_INET]

netifaces.ifaddresses('lo')[netifaces.AF_INET][0]['addr']
netifaces.ifaddresses('eth0')[netifaces.AF_INET][0]['addr']

netifaces.ifaddresses('lo')[netifaces.AF_INET][0]['netmask']
netifaces.ifaddresses('eth0')[netifaces.AF_INET][0]['netmask']

import ipaddress
ipaddress.ip_address('127.0.0.1')
ipaddress.ip_address('8.8.8.8')
ipaddress.ip_address('8.8.8.8') + 1
ipaddress.ip_address
