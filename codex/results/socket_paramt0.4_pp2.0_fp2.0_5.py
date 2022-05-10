import socket
socket.if_indextoname(1)

# socket.if_nameindex()
# Return a list of network interface information
# Return a list of tuples containing the interface name and index of all the interfaces found on the host
socket.if_nameindex()

# socket.if_nametoindex(if_name)
# Return the interface index of the given interface name
socket.if_nametoindex('lo0')

# socket.if_nameindex()
# Return the interface name of the given interface index
socket.if_indextoname(1)

# socket.inet_aton(ip_string)
# Convert an IP address from string format to 32-bit packed binary format
socket.inet_aton('127.0.0.1')

# socket.inet_ntoa(packed_ip)
# Convert a 32-bit packed IPv4 address (a string four characters in length) to its standard dotted-quad string representation
socket.inet_ntoa(b'\x7f\x00\x00\x01')

# socket.inet_pton(address_family, ip_string)
# Convert an IP address from
