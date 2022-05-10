import socket
socket.if_indextoname(0)

import subprocess
proc = subprocess.Popen("ifconfig", stdout=subprocess.PIPE)
output = proc.stdout.read()
print (output)

import netifaces
netifaces.interfaces()

import netifaces
print netifaces.ifaddresses('eth1')[netifaces.AF_LINK]

import netifaces
print netifaces.ifaddresses('eth1')[netifaces.AF_INET]

import netifaces
print netifaces.ifaddresses('eth1')[netifaces.AF_INET][0]['addr']

import netifaces
print netifaces.ifaddresses('eth1')[netifaces.AF_INET][0]['netmask']

import netifaces
print netifaces.ifaddresses('eth1')[netifaces.AF_INET][0]['broadcast']

import netifaces
print netifaces.ifaddresses('eth1')[netifaces.AF_INET][0]['peer']

