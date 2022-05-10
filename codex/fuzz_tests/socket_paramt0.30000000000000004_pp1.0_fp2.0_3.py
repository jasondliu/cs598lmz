import socket
socket.if_indextoname(3)

# get the MAC address of the interface
import uuid
mac = uuid.getnode()

# convert the MAC address to a string
mac_string = ':'.join(("%012X" % mac)[i:i+2] for i in range(0, 12, 2))

# print the MAC address
print(mac_string)

# get the IP address
import socket
ip = socket.gethostbyname(socket.gethostname())

# print the IP address
print(ip)

# get the hostname
import socket
hostname = socket.gethostname()

# print the hostname
print(hostname)

# get the DNS server
import socket
dns = socket.gethostbyname_ex('www.google.com')[2]

# print the DNS server
print(dns)

# get the DNS server
import socket
dns = socket.gethostbyname_ex('www.google.com')[2]

# print the DNS server
print(dns)

# get the DNS server
import socket
