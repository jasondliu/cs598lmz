import socket
# Test socket.if_indextoname

set_admin()

index = 8
if_name = socket.if_indextoname( index )
if if_name != 'lo':
	print "if_indextoname(",index,") failed"
