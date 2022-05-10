import socket
socket.if_indextoname(3)

import netifaces
netifaces.ifaddresses('eth0')

import netifaces
netifaces.ifaddresses('eth0')[netifaces.AF_LINK]

import netifaces
netifaces.ifaddresses('eth0')[netifaces.AF_LINK][0]['addr']

import netifaces
netifaces.ifaddresses('eth0')[netifaces.AF_INET6][0]['addr']

import netifaces
netifaces.ifaddresses('eth0')[netifaces.AF_INET][0]['addr']

import netifaces
netifaces.ifaddresses('eth0')[netifaces.AF_INET][0]['netmask']

import netifaces
netifaces.ifaddresses('eth0')[netifaces.AF_INET][0]['broadcast']

import netifaces
netifaces.gateways()

import netifaces
