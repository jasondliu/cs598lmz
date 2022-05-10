import socket
socket.if_indextoname('0')

# If you have a line like this in your /etc/network/interfaces file
#    iface eth0 inet6 dhcp
# Then you can get the IPv6 address with this
addrinfo = socket.getaddrinfo('eth0', None, socket.AF_INET6, socket.SOCK_DGRAM, 0, socket.AI_CANONNAME)[0]
ip = addrinfo[4][0]


# This works for all address types
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("google.com",80))
ip = s.getsockname()[0]
