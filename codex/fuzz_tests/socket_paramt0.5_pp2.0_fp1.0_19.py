import socket
socket.if_indextoname(3)

# if_nametoindex()
# if_nametoindex() returns the integer index of the given interface name
# If the interface does not exist, it raises an error
socket.if_nametoindex('lo')

# if_nameindex()
# if_nameindex() returns a list of tuples containing the interface name and integer index
# If there are no interfaces, an empty list is returned
socket.if_nameindex()

# if_nametoindex()
# if_nametoindex() returns the integer index of the given interface name
# If the interface does not exist, it raises an error
socket.if_nametoindex('lo')

# if_nameindex()
# if_nameindex() returns a list of tuples containing the interface name and integer index
# If there are no interfaces, an empty list is returned
socket.if_nameindex()

# gethostname()
# gethostname() returns the name of the host
socket.gethostname()

# gethostbyname()
# gethostbyname() returns the IP address of the hostname
socket.gethostby
