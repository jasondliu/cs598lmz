import socket
socket.if_indextoname(2)

import netifaces
netifaces.ifaddresses('eth0')
netifaces.ifaddresses('eth0')[netifaces.AF_INET][0]['addr']

import netifaces
netifaces.ifaddresses('lo')
netifaces.ifaddresses('lo')[netifaces.AF_LINK]
netifaces.ifaddresses('lo')[netifaces.AF_LINK][0]['addr']

import netifaces
netifaces.interfaces()
netifaces.ifaddresses('eth0')
netifaces.ifaddresses('eth0')[netifaces.AF_INET]
netifaces.ifaddresses('eth0')[netifaces.AF_INET][0]['addr']

import netifaces
netifaces.ifaddresses('lo')
netifaces.ifaddresses('lo')[netifaces.AF_LINK]
netifaces.ifaddresses('lo')[netifaces.AF_LINK][0]['addr']

import netif
