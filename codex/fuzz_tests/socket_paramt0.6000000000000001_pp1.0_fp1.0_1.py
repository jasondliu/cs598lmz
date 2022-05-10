import socket
socket.if_indextoname(3)

#if_nametoindex(ifname)
#Return the interface index of the interface with the given name. Raise IOError if the interface doesn't exist.
socket.if_nametoindex('eth0')

#if_nameindex()
#Return a list of (ifindex, ifname) tuples, one for each interface on the machine. The list is in arbitrary order.
socket.if_nameindex()

#if_nametoindex(ifname)
#Return the interface index of the interface with the given name. Raise IOError if the interface doesn't exist.
socket.if_nametoindex('eth0')

#if_nameindex()
#Return a list of (ifindex, ifname) tuples, one for each interface on the machine. The list is in arbitrary order.
socket.if_nameindex()

#socket.getaddrinfo(host, port, family=0, type=0, proto=0, flags=0)
#Translate the host/port argument into a sequence of 5-tuples that contain all the necessary arguments for creating a socket connected to that service.
#
