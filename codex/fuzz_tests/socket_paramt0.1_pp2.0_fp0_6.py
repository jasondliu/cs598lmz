import socket
socket.if_indextoname(3)

# 'en0'

# socket.if_nameindex()
# Return a list of network interface information.
# Each element of the list is a tuple containing a string
# representing the interface name and an integer representing
# the interface index.

socket.if_nameindex()

# [(1, 'lo0'), (2, 'gif0'), (3, 'stf0'), (4, 'en0'), (5, 'en1'), (6, 'fw0'), (7, 'vmnet1'), (8, 'vmnet8')]

# socket.if_nametoindex(if_name)
# Return the interface index corresponding to the given interface name.

socket.if_nametoindex('en0')

# 4

# socket.gethostbyaddr(ip_address)
# Return a triple (hostname, aliaslist, ipaddrlist) where hostname is the primary host name responding to the given ip_address, aliaslist is a (possibly empty) list of alternative host names for the same address, and ipaddrlist is a list of IPv4/v6 addresses for the
