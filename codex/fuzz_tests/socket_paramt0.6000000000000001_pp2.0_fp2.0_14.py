import socket
socket.if_indextoname(1)

# Get the IP address of the interface.
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
print s.getsockname()[0]

# Get the MAC address of the interface.
import netifaces
print netifaces.ifaddresses('eth0')[netifaces.AF_LINK][0]['addr']

# Get the IP address of the interface.
print netifaces.ifaddresses('eth0')[netifaces.AF_INET][0]['addr']

# Get the netmask of the interface.
print netifaces.ifaddresses('eth0')[netifaces.AF_INET][0]['netmask']

# Get the broadcast address of the interface.
print netifaces.ifaddresses('eth0')[netifaces.AF_INET][0]['broadcast']

# Get the IP addresses of all the interfaces.
print netifaces.interfaces()

# Get the MAC addresses of
