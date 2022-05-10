import socket
socket.if_indextoname(3)

# socket.if_nameindex()
# Return a list of network interface information.
# Each element in the list is a tuple that contains the following:
#     interface index
#     interface name
#
# The list is sorted by the interface index.
#
# Example:
#
#     [(1, 'lo'), (2, 'eth0'), (3, 'eth1')]
#
# Availability: Unix.

socket.if_nameindex()

# socket.if_nametoindex(if_name)
# Return the interface index of an interface name.
#
# Availability: Unix.

socket.if_nametoindex('eth0')

# socket.gethostbyname(hostname)
# Return the IP address (a string of the form '255.255.255.255') for a host.
#
# Availability: Unix, Windows.

socket.gethostbyname('google.com')

# socket.gethostbyname_ex(hostname)
# Return a triple (hostname, aliaslist, ipaddrlist) where hostname is the
#
