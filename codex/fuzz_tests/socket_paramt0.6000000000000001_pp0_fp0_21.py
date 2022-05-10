import socket
socket.if_indextoname(3)

# Run this to get the interface name
# import netifaces
# netifaces.interfaces()

# Run this to get a list of all the addresses on that interface
# netifaces.ifaddresses('enp0s8')

# Run this to get the ipv4 address
# netifaces.ifaddresses('enp0s8')[netifaces.AF_INET]

# Run this to get the mac address
# netifaces.ifaddresses('enp0s8')[netifaces.AF_LINK]

# Run this to get the ipv6 address
# netifaces.ifaddresses('enp0s8')[netifaces.AF_INET6]

# Run this to get the address of the gateway
# netifaces.gateways()

# Run this to get the address of the loopback interface
# netifaces.ifaddresses('lo')

# Run this to get the address of the loopback interface
# netifaces.ifaddresses('lo')

# Run this to get the address of
