import socket
socket.if_indextoname('3')

'''
import socket
for i in range(8,10):
	try:
		print(socket.if_indextoname(i))
	except:
		pass
'''

# Find the interface name with a given IPv4 address
# gethostbyaddr(ip_address)

# Find the IPv4 address(es) of a given interface name
# gethostbyname(interface_name)

# Convert a 32-bit integer (IPv4 address) to its standard dotted
# decimal representation as a string
# socket.inet_aton(ip_address_as_int)

# Convert a 32-bit integer (IPv4 address) to its binary representation
# as a bytes object
# socket.inet_ntoa(ip_address_as_int)

#import socket
#print(dir(socket))
