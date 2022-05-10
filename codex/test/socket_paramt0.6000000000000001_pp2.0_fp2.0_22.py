import socket
socket.if_indextoname('3')

# list all interfaces
import netifaces
netifaces.interfaces()

# list all addresses
netifaces.ifaddresses('en0')
netifaces.ifaddresses('eth0')

# get the ipv4 address
netifaces.ifaddresses('en0')[netifaces.AF_INET][0]['addr']
netifaces.ifaddresses('eth0')[netifaces.AF_INET][0]['addr']

# get the ipv6 address
netifaces.ifaddresses('en0')[netifaces.AF_INET6][0]['addr']
netifaces.ifaddresses('eth0')[netifaces.AF_INET6][0]['addr']

# get the MAC address
netifaces.ifaddresses('en0')[netifaces.AF_LINK][0]['addr']
netifaces.ifaddresses('eth0')[netifaces.AF_LINK][0]['addr']
