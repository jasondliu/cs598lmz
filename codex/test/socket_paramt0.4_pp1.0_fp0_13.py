import socket
socket.if_indextoname(3)

# get the MAC address of the interface
import netifaces
netifaces.ifaddresses('eth0')[netifaces.AF_LINK][0]['addr']

# get the IP address of the interface
import netifaces
netifaces.ifaddresses('eth0')[netifaces.AF_INET][0]['addr']

# get the broadcast address of the interface
import netifaces
netifaces.ifaddresses('eth0')[netifaces.AF_INET][0]['broadcast']

# get the netmask of the interface
import netifaces
netifaces.ifaddresses('eth0')[netifaces.AF_INET][0]['netmask']

# get the network address of the interface
import netifaces
netifaces.ifaddresses('eth0')[netifaces.AF_INET][0]['addr']
netifaces.ifaddresses('eth0')[netifaces.AF_INET][0]['netmask']

# get the default gateway
import netifaces

