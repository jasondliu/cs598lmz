import socket
socket.if_indextoname(3)

# get the IP address of the default gateway
import netifaces
netifaces.gateways()['default'][netifaces.AF_INET][0]

# get the IP address of all interfaces
netifaces.ifaddresses('eth0')[netifaces.AF_INET][0]['addr']

# get the MAC address of all interfaces
netifaces.ifaddresses('eth0')[netifaces.AF_LINK][0]['addr']

# get the MTU of all interfaces
netifaces.ifaddresses('eth0')[netifaces.AF_LINK][0]['addr']

# get the broadcast address of all interfaces
netifaces.ifaddresses('eth0')[netifaces.AF_INET][0]['broadcast']

# get the netmask of all interfaces
netifaces.ifaddresses('eth0')[netifaces.AF_INET][0]['netmask']

# get the IP address of all interfaces
