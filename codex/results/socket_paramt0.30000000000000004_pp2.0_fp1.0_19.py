import socket
socket.if_indextoname(3)

# Get the IP address of an interface
import socket
socket.if_nameindex()

# Get the MAC address of an interface
import netifaces
netifaces.ifaddresses('eth0')[netifaces.AF_LINK][0]['addr']

# Get the IP address of an interface
import netifaces
netifaces.ifaddresses('eth0')[netifaces.AF_INET][0]['addr']

# Get the broadcast address of an interface
import netifaces
netifaces.ifaddresses('eth0')[netifaces.AF_INET][0]['broadcast']

# Get the netmask of an interface
import netifaces
netifaces.ifaddresses('eth0')[netifaces.AF_INET][0]['netmask']

# Get the MAC address of an interface
import netifaces
netifaces.ifaddresses('eth0')[netifaces.AF_LINK][0]['addr']

# Get the IP address of an interface
import netifaces
netifaces.
