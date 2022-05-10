import socket
socket.if_indextoname(psutil.net_if_addrs()[i][j].family, psutil.net_if_addrs()[i][j].address)

# if you want to know the name of the network interface
# of the first IPv4 address of the first network interface
socket.if_indextoname(psutil.net_if_addrs()[0][0].family, psutil.net_if_addrs()[0][0].address)

# if you want to know the name of the network interface
# of the second IPv4 address of the first network interface
socket.if_indextoname(psutil.net_if_addrs()[0][1].family, psutil.net_if_addrs()[0][1].address)

# if you want to know the name of the network interface
# of the first IPv6 address of the first network interface
socket.if_indextoname(psutil.net_if_addrs()[0][2].family, psutil.net_if_addrs()[0][2].address)

# if you want to know
