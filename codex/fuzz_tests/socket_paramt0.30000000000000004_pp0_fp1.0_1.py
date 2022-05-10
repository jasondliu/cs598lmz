import socket
socket.if_indextoname(1)

# if_nametoindex(ifname)
# Return the interface index corresponding to the given interface name.
# An exception is raised if the interface doesn’t exist.
#
# New in version 3.3.
socket.if_nametoindex('lo')

# if_nameindex()
# Return a list of (index, name) tuples for all interfaces.
#
# New in version 3.3.
socket.if_nameindex()

# if_nametoindex(ifname)
# Return the interface index corresponding to the given interface name.
# An exception is raised if the interface doesn’t exist.
#
# New in version 3.3.
socket.if_nametoindex('lo')

# if_nameindex()
# Return a list of (index, name) tuples for all interfaces.
#
# New in version 3.3.
socket.if_nameindex()

# gethostbyname(hostname)
# Translate a host name to IPv4 address format. The IPv4 address is returned as a string, such as ‘100.50
