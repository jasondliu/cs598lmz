import socket
socket.if_indextoname(1)

# Output: 'lo'

# Get the interface index for a given interface name
socket.if_nametoindex('lo')

# Output: 1

# Get the MAC address for a given interface name
socket.if_nameindex()

# Output: [(1, 'lo')]

# Get the MAC address for a given interface name
socket.if_nameindex(1)

# Output: 'lo'

# Get the MAC address for a given interface name
socket.if_nameindex('lo')

# Output: 1

# Get the MAC address for a given interface name
socket.if_nameindex(['lo'])

# Output: [(1, 'lo')]

# Get the MAC address for a given interface name
socket.if_nameindex(['lo', 'eth0'])

# Output: [(1, 'lo'), (2, 'eth0')]

# Get the MAC address for a given interface name
socket.if_nameindex(['lo', 'eth0', 'eth1'])

# Output: [(1, 'lo'),
