import socket
socket.if_indextoname(3)

# Initialize variables
interface       = ""
target_ip       = "192.168.1.100"
gateway_ip      = "192.168.1.1"
packet_count    = 1000

# Set confiuration of target IP and gateway IP
conf.iface = interface

# read in the host to MAC address
conf.verb  = 0
ans, unans = srp(Ether(dst = "ff:ff:ff:ff:ff:ff")/ARP(pdst = target_ip), timeout = 2, iface = interface, inter = 0.1)

# print out the result
