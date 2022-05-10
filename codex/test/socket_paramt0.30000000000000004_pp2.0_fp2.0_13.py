import socket
socket.if_indextoname(3)

# socket.if_nameindex()
# Return a list of network interface information, in the form of a list of (if_index, if_name) tuples.
# The list is sorted by interface index.
socket.if_nameindex()

# socket.if_nametoindex(if_name)
# Return the interface index of the interface if_name.
# If the interface does not exist, OSError is raised.
socket.if_nametoindex('lo')

# socket.gethostbyaddr(host)
# Return a triple (hostname, aliaslist, ipaddrlist) where hostname is the primary host name responding to the given ip_address,
# aliaslist is a (possibly empty) list of alternative host names for the same address, and ipaddrlist is a list of IPv4/v6 addresses
# for the same interface on the same host (most likely containing only a single address).
# To find the hostname for a given address, use socket.gethostbyaddr(ip_address).
socket.gethostbyaddr('127.0.0.1')

# socket
