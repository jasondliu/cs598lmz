import socket
socket.if_indextoname(3)

# If you want to know the name of the interface, you can use the if_nameindex() function.
# This function returns a list of tuples with the interface index and name.

socket.if_nameindex()

# You can also use the if_nametoindex() function to get the index of an interface given its name.

socket.if_nametoindex('lo')

# To get the MAC address of an interface, you can use the if_hwaddr() function.
# This function returns a tuple with the interface index, the MAC address, and the maximum transmission unit (MTU) of the interface.

socket.if_hwaddr(3)

# If you want to get the IP address of an interface, you can use the if_addr() function.
# This function returns a list of tuples with the interface index, the address family, and the IP address.

socket.if_addr(3)

# If you want to get the broadcast address of an interface, you can use the if_brdaddr() function.
# This function returns a tuple with the interface index, the address family
