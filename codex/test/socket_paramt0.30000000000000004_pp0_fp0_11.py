import socket
socket.if_indextoname(1)

# socket.if_nameindex()
# Return a list of network interface information.
# Each element of the list is a tuple containing a string giving the interface name, and an integer giving the corresponding index.
socket.if_nameindex()

# socket.if_nametoindex(if_name)
# Return the interface index corresponding to the given interface name.
socket.if_nametoindex('lo')

# socket.gethostbyaddr(ip_address)
# Return a triple (hostname, aliaslist, ipaddrlist) where hostname is the primary host name responding to the given ip_address, aliaslist is a (possibly empty) list of alternative host names for the same address, and ipaddrlist is a list of IPv4/v6 addresses for the same interface on the same host (most likely containing only a single address).
socket.gethostbyaddr('127.0.0.1')

# socket.gethostbyname(hostname)
# Return a triple (hostname, aliaslist, ipaddrlist) where hostname is the primary host name responding to the given ip_address, aliaslist is a
