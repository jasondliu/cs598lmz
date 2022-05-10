import socket
socket.if_indextoname(12)

#Converting interface names to their IP addresses
#>>> import socket
#>>> socket.if_nameindex()
#[(1, 'lo'), (2, 'eth0'), (3, 'eth1')]

import socket
socket.if_nameindex()

#Converting interface names to their IP addresses
#>>> import socket
#>>> socket.if_nameindex()
#[(1, 'lo'), (2, 'eth0'), (3, 'eth1')]

#>>> socket.if_nameindex(2)
#[('lo', 1), ('eth0', 2)]

#>>> socket.if_nameindex(3)
#[('lo', 1), ('eth0', 2), ('eth1', 3)]

#>> socket.if_nameindex(2)
#[('lo', 1), ('eth0', 2)]

import socket
socket.if_nameindex()
socket.if_nameindex(2)
socket.if_nameindex(3)

#Converting host address to hostname
#>>> import socket
#>>> socket.gethost
