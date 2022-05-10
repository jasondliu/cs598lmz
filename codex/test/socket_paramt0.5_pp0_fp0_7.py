import socket
socket.if_indextoname(3)

# get the IP address of the default gateway
gw = netifaces.gateways()['default'][netifaces.AF_INET][0]

# create an ARP request
packet = Ether(dst='ff:ff:ff:ff:ff:ff')/ARP(op=1, pdst=gw)

# send the packet and accept the response
resp, unans = srp(packet, iface=iface, timeout=2, verbose=0)

# extract the MAC address from the response
mac = resp[0][1][Ether].src

# print the result
