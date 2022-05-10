import socket
# Test socket.if_indextoname()
for i in range(10):
	try:
		name = socket.if_indextoname(i)
	except:
		print('%d: No interface' % i)
	else:
		print(name)
