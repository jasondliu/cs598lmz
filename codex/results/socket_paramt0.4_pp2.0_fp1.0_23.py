import socket
socket.if_indextoname(4)

#Get all interfaces
import netifaces
netifaces.interfaces()

#Get all addresses on an interface
netifaces.ifaddresses('eth0')

#Get the IPv4 address of an interface
netifaces.ifaddresses('eth0')[netifaces.AF_INET][0]['addr']

#Get the MAC address of an interface
netifaces.ifaddresses('eth0')[netifaces.AF_LINK][0]['addr']

#Get all gateway addresses on the system
netifaces.gateways()

#Get the default gateway
netifaces.gateways()['default'][netifaces.AF_INET]

#Get the IPv4 address of the default gateway
netifaces.gateways()['default'][netifaces.AF_INET][0]

#Get the MAC address of the default gateway
netifaces.gateways()['default'][netifaces.AF_INET][1]

#Get the default IPv6 gateway
netifaces.gateways()['default'][netif
