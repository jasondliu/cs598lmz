import socket
socket.if_indextoname(13)

# if_indextoname(ifindex)
# If a valid interface index is given, return the corresponding interface name.
# Otherwise return ValueError.
#
# Raises:
#   ValueError: An invalid interface index was given.
#
# New in version 3.2.

# ifindex is the index of the interface to be queried.

# Changed in version 3.3:
#   If the given interface index is valid, return the corresponding interface name.
#   Otherwise return ValueError.

# Changed in version 3.4:
#   If the given interface index is valid, return the corresponding interface name.
#   Otherwise return ValueError.

# socket.if_nameindex()
# Return a list of tuples containing interface indices and human-readable names for all interfaces.
#
# The indices and names are retrieved from the operating system, and may not be consecutive or ordered.
#
# New in version 3.2.

# Changed in version 3.3:
#   If there is at least one interface, return a list of tuples containing the interface indices and names.
#
