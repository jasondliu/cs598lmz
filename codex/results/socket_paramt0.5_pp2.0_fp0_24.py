import socket
socket.if_indextoname(5)

#if_nameindex()
#Return the list of network interfaces available on the system
#Example:
import socket
socket.if_nameindex()

#if_nametoindex(if_name)
#Return the index of the interface if_name
#Example:
import socket
socket.if_nametoindex('lo')

#inet_aton(ip_string)
#Convert an IP address from its dotted-decimal format to 32-bit packed binary format, as a bytes object
#Example:
import socket
socket.inet_aton('127.0.0.1')

#inet_ntoa(packed_ip)
#Convert an IP address from 32-bit packed binary format to its standard dotted-decimal representation
#Example:
import socket
socket.inet_ntoa(b'\x7f\x00\x00\x01')

#inet_pton(address_family, ip_string)
#Convert an IP address from its family-specific string format to a packed, binary format
#Example:
import socket
socket.inet_pton(socket.AF
