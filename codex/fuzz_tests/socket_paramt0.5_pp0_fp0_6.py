import socket
socket.if_indextoname(3)

# if_indextoname(3)
#       Convert an interface index in host byte order to an interface name,
#       returning a string of the form 'em0'.

#       The index should have been obtained from a call to if_nametoindex()
#       or if_nametoindex(3).  If no interface corresponds to the given
#       index, NULL is returned.

#       When the sockfd argument is not -1, the interface name is checked
#       against the list of interfaces associated with the socket.  If the
#       interface name is not on the list, the function fails and returns
#       NULL.

#       The sockfd argument is ignored on Linux.

# RETURN VALUE
#       On success, if_indextoname() returns a pointer to the interface name.
#       On failure, NULL is returned and errno is set to indicate the error.

# ERRORS
#       EINVAL The index argument is not a valid interface index.

#       ENXIO  The interface corresponding to the given index does not exist.

#       ENOMEM
