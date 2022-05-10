import socket
socket.if_indextoname(2)

import netifaces
print netifaces.interfaces()

print netifaces.gateways()
print netifaces.gateways()['default'][netifaces.AF_INET]

#print netifaces.ifaddresses('wlan0')

netifaces.ifaddresses('wlan0')[netifaces.AF_LINK]

print netifaces.ifaddresses('wlan0')[netifaces.AF_LINK][0]['addr']

print netifaces.ifaddresses('wlan0')[netifaces.AF_INET][0]['addr']
