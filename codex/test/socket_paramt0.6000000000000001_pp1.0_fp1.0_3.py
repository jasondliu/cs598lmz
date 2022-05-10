import socket
socket.if_indextoname('3')

# The following should be equivalent to the above
import netifaces
netifaces.if_name(3)

# The following should print the MAC address of the interface
netifaces.ifaddresses('eth0')[netifaces.AF_LINK][0]['addr']

# The following should print the IPv4 address
netifaces.ifaddresses('eth0')[netifaces.AF_INET][0]['addr']
