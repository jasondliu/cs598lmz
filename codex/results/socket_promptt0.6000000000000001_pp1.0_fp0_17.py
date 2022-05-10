import socket
# Test socket.if_indextoname() for invalid ifindex
# This is an invalid ifindex and should throw an error
ifindex = 1
try:
	address = socket.if_indextoname(ifindex)
except socket.error as e:
	print("socket.error: %s" %e)

# Test socket.if_indextoname() for valid ifindex
# This is a valid ifindex and should not throw an error
ifindex = 3
try:
	address = socket.if_indextoname(ifindex)
except socket.error as e:
	print("socket.error: %s" %e)
