import socket
socket.if_indextoname(3)

# if_indextoname(3)
#       Convert an interface index number into its corresponding name.
#       This is the reverse of if_nametoindex(3).
#
#       The if_indextoname() function maps the interface index number
#       given in index to its corresponding name.  The name is copied
#       into the buffer pointed to by ifname, which must be a buffer of
#       at least IF_NAMESIZE bytes.  The buffer must be aligned on a
#       suitable boundary for the type of the buffer.
#
#       The if_indextoname() function returns a pointer to the buffer
#       containing the interface name, or NULL if the index is not
#       known.
#
#       The if_indextoname() function may fail if:
#
#           ENXIO     The specified index does not exist.
#
#       The if_indextoname() function first appeared in Linux 2.2.
#
# SEE ALSO
#       if_nameindex(3), if_nametoindex(3), if_freenameindex(
