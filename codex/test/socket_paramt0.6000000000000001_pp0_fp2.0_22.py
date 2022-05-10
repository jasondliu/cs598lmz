import socket
socket.if_indextoname('1')

# get a list of all interfaces
socket.if_nameindex()

# get a list of all interfaces
socket.if_nameindex()

# get the name of a specific interface by index
socket.if_indextoname(1)

# get the index of a specific interface by name
socket.if_nametoindex('lo0')

# get the MAC address of a specific interface by index
socket.if_indextomac(1)

# get the MAC address of a specific interface by name
socket.if_nametomac('lo0')
