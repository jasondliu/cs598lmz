import socket
socket.if_indextoname(2)

# socket.if_nametoindex(ifname)
# Return the interface index of the interface named ifname.
# This is a small integer, suitable for use in C level code.
# On error, raise OSError.
socket.if_nametoindex('eth0')

# socket.if_nameindex()
# Return a list of (ifname, ifindex) tuples.
# The list is built from the interfaces available on the local system.
# The interfaces are listed in no particular order.
# This is a snapshot of the system at the time of the call, and the result
# is not updated if new interfaces are added later.
# The list is empty if there are no interfaces.
socket.if_nameindex()

# socket.if_nametoindex(ifname)
# Return the interface index of the interface named ifname.
# This is a small integer, suitable for use in C level code.
# On error, raise OSError.
socket.if_nametoindex('eth0')

# socket.if_nameindex()
# Return a list of (if
