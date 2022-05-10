import socket
# Test socket.if_indextoname()
#
# The if_indextoname function translates an interface index into an
# interface name. The interface name is a null-terminated string.
#
# The if_indextoname function returns a pointer to the interface name
# associated with the interface index, or NULL if there is no such
# association (e.g., if the interface index is invalid).
print socket.if_indextoname(1)
# Test socket.if_nameindex()
#
# The if_nameindex function returns an array of if_nameindex structures.
# The last element of the array has an interface index of zero with
# the appropriate member variables loaded with zeros.
#
# The if_nameindex function returns a null pointer if an error occurs
# (e.g., if there are no interfaces on the host).
print socket.if_nameindex()
print socket.if_nameindex(9)
print socket.if_nameindex(0)
# Test socket.if_nametoindex()
#
# The if_nametoindex function translates an interface name into an
# interface index.
#
#
