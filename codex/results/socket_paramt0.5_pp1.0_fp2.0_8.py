import socket
socket.if_indextoname(3)

# get all interfaces on the machine
import psutil
psutil.net_if_addrs()

# get the first interface name
psutil.net_if_addrs().keys()[0]

# get the MAC address of the first interface
mac_addr = psutil.net_if_addrs()[psutil.net_if_addrs().keys()[0]][0][1]

# get the IP address of the first interface
ip_addr = psutil.net_if_addrs()[psutil.net_if_addrs().keys()[0]][1][1]

# get the IP address of the first interface
ip_addr = psutil.net_if_addrs()[psutil.net_if_addrs().keys()[0]][1][1]

# get the IP address of the first interface
ip_addr = psutil.net_if_addrs()[psutil.net_if_addrs().keys()[0]][1][1]

# get the IP address of the first interface
ip_addr = ps
