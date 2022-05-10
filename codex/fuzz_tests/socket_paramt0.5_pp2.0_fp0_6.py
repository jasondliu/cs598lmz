import socket
socket.if_indextoname(3)

# if_indextoname(3)
#       The  if_indextoname()  function  maps  an interface index to its corresponding name.  The
#       if_nametoindex() function performs the inverse mapping.

#       The  if_indextoname()  function  takes  a  single  integer argument, an interface index.  If
#       successful, it returns the corresponding interface name as a string.  Otherwise, it returns
#       None.

#       The  if_indextoname()  function  is  available  on  Linux  2.2 and later and on BSD variants.

#       See also the socket.if_nameindex() function, which returns a list of all interfaces and
#       their corresponding interface indexes.

# SEE ALSO
#       if_nameindex(3), if_nametoindex(3), socket(7)

# COLOPHON
#       This  page  is  part of release 4.04 of the Linux man-pages project.  A description of the
#       project, information about reporting bugs, and the latest version
