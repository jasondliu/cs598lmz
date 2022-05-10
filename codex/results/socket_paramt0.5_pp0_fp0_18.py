import socket
socket.if_indextoname(3)

# 'en0'

# to find the interface name for a given IP address
socket.if_nametoindex('en0')

# 3

# to find the address for a given interface name
socket.if_nameindex()

# [(1, 'lo0'), (2, 'gif0'), (3, 'stf0'), (4, 'en0'), (5, 'en1'), (6, 'fw0'), (7, 'vmnet1'), (8, 'vmnet8')]

# to find the address for a given interface name
socket.if_nameindex()

# [(1, 'lo0'), (2, 'gif0'), (3, 'stf0'), (4, 'en0'), (5, 'en1'), (6, 'fw0'), (7, 'vmnet1'), (8, 'vmnet8')]

# to find the address for a given interface name
socket.if_nameindex()

# [(1, 'lo0'), (2, 'gif0'), (3, 'stf0'), (4, 'en0
