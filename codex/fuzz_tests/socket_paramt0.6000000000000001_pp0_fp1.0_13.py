import socket
socket.if_indextoname(3)

#for i in range(1,10):
#	try:
#		print socket.if_indextoname(i)
#	except:
#		print 'not found'

#print socket.if_indextoname(1)
print socket.if_nameindex()
print socket.if_nametoindex('eth0')
print socket.if_nameindex()[socket.if_nametoindex('eth0')][1]

print socket.gethostname()
print socket.gethostbyname('localhost')
print socket.gethostbyname_ex('localhost')
#print socket.gethostbyaddr('127.0.0.1')
#print socket.gethostbyaddr('127.0.1.1')
print socket.gethostbyname_ex('localhost')[2]

print socket.gethostbyname_ex('localhost')[2]

print socket.gethostbyname_ex('localhost')[2]

print socket.gethostbyname_ex('localhost')[2]
