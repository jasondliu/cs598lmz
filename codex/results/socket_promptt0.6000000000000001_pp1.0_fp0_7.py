import socket
# Test socket.if_indextoname() on a valid interface name
socket.if_indextoname('0')

# Test socket.if_indextoname() on an invalid interface name
try:
	socket.if_indextoname('-1')
except OverflowError:
	print('OverflowError')

# Test socket.if_indextoname() on a large interface index
# socket.if_indextoname(str(sys.maxsize + 1))

# Test socket.if_indextoname() on a small interface index
try:
	socket.if_indextoname('-2')
except OverflowError:
	print('OverflowError')
