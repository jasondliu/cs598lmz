import socket
# Test socket.if_indextoname()
netifaces.if_indextoname(1)

# Test socket.if_nameindex()
netifaces.if_nameindex()

# Test socket.if_nametoindex()
netifaces.if_nametoindex('lo')

# Test netifaces.ifaddresses()
netifaces.ifaddresses('lo')

# Test netifaces.interfaces()
netifaces.interfaces()

# Test netifaces.gateways()
netifaces.gateways()

# Test netifaces.AF_LINK
netifaces.AF_LINK

# Test netifaces.AF_INET
netifaces.AF_INET

# Test netifaces.AF_INET6
netifaces.AF_INET6

# Test netifaces.AF_PACKET
netifaces.AF_PACKET

# Test netifaces.AF_BRIDGE
netifaces.AF_BRIDGE

# Test netifaces.socket.AF_PACKET
