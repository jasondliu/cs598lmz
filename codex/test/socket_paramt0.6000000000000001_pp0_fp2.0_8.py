import socket
socket.if_indextoname(interface)

# Now we have the name, we can get the MAC address:

import netifaces
netifaces.ifaddresses(interface)
netifaces.ifaddresses(interface)[netifaces.AF_LINK]
netifaces.ifaddresses(interface)[netifaces.AF_LINK][0]['addr']

# Now, to get the IP address, we use the command 'gethostbyname'
# This returns a triple: the hostname, the alias list, and the IP address

socket.gethostbyname(socket.gethostname())

# This is the IPv4 address. To get the IPv6 address, we can use the
# socket 'getaddrinfo' command:

socket.getaddrinfo(socket.gethostname(), 80)[0][4][0]

# So, we can put all of this together and print out the information:

import netifaces
import socket

# Get all of the interfaces on the system:

interfaces = netifaces.interfaces()

# For each interface, print out the name, the IP address and
