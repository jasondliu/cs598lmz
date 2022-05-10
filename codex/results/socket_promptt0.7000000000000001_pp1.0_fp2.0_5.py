import socket
# Test socket.if_indextoname in netifaces.
print(netifaces.if_indextoname(1))
# Test socket.if_nametoindex in netifaces.
print(netifaces.if_nametoindex('eth0'))

# TODO(bpeckham): Further testing of netifaces.interfaces,
# netifaces.ifaddresses, and netifaces.address_families.

# Test netifaces.gateways.
print(netifaces.gateways())

# Test netifaces.AF_INET.
print(netifaces.AF_INET)

# Test netifaces.AF_INET6.
print(netifaces.AF_INET6)

# Test netifaces.AF_LINK.
print(netifaces.AF_LINK)

# Test netifaces.AF_PACKET.
print(netifaces.AF_PACKET)

# Test netifaces.AF_UNIX.
print(netifaces.AF_UNIX)

# Test netifaces.AF_UN
