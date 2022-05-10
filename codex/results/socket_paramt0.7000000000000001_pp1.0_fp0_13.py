import socket
socket.if_indextoname('1')

# A list of all the IPv4 interfaces
socket.if_nameindex()

# A list of all the IPv6 interfaces
socket.if_nameindex(family=socket.AF_INET6)

# A list of all the IPv4 and IPv6 interfaces
socket.if_nameindex(family=socket.AF_UNSPEC)

# A tuple with the interface index and the interface name
socket.if_nametoindex('lo')

# The same, but with an IPv6 interface
socket.if_nametoindex('lo', family=socket.AF_INET6)

# The same, but with an IPv4 interface
socket.if_nametoindex('lo', family=socket.AF_INET)

# The IP address of the interface
socket.if_nameindex(family=socket.AF_INET6)[0][1][:-1]

# The IP address of the interface
socket.if_nameindex(family=socket.AF_INET)[0][1]

# The IP address of the interface
socket.if_nameindex(family=socket.
