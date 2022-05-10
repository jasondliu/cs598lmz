import socket
socket.if_indextoname(3)

#ifconfig
#ifconfig en0
#ifconfig en0 | grep inet
#ifconfig en0 | grep inet | grep -v inet6 | cut -d ' ' -f2
#ifconfig en0 | grep inet | grep -v inet6 | cut -d ' ' -f2 | cut -d ':' -f2

import netifaces
netifaces.interfaces()
netifaces.ifaddresses('en0')
netifaces.ifaddresses('en0')[netifaces.AF_INET]

#ifconfig
#ifconfig en0
#ifconfig en0 | grep ether | cut -d ' ' -f2

import netifaces
netifaces.interfaces()
netifaces.ifaddresses('en0')
netifaces.ifaddresses('en0')[netifaces.AF_LINK]

#ifconfig
#ifconfig en0
#ifconfig en0 | grep ether | cut -d ' ' -f2

import netifaces
netifaces.interfaces()
netif
