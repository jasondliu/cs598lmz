import socket
socket.if_indextoname(3)

# if_indextoname(3)
#     if_indextoname() returns the name of the interface associated with the
#     specified index.
#
#     The if_indextoname() function is the inverse of if_nametoindex(3).
#
#     The if_indextoname() function is not thread-safe.  If multiple threads
#     use this function, then the caller must provide its own protection
#     against simultaneous invocations.
#
#     The if_indextoname() function is available on Linux since kernel
#     2.2.
#
#     On Linux, the if_indextoname() function is a library function that uses
#     the routing socket to obtain the interface name corresponding to the
#     specified index.
#
#     On Linux, the if_indextoname() function is a library function that uses
#     the routing socket to obtain the interface name corresponding to the
#     specified index.  This function can also be used to obtain the
#     interface name corresponding to the index returned by if_nametoindex(3).

