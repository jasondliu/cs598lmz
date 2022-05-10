import socket
# Test socket.if_indextoname()
print (socket.if_indextoname(1))
# Test socket.if_nameindex()
print (socket.if_nameindex())
# Test socket.if_nameindex()
print (socket.if_nametoindex('lo'))
# Test socket.if_nameindex()
print (socket.if_nametoindex('eth0'))
# Test socket.if_nameindex()
print (socket.if_nametoindex('wlan0'))
# Test socket.if_nameindex()
print (socket.if_nametoindex('ppp0'))

# Test socket.gethostbyname()
print (socket.gethostbyname('localhost'))

# Test socket.gethostbyaddr()
print (socket.gethostbyaddr('127.0.0.1'))

# Test socket.gethostname()
print (socket.gethostname())

# Test socket.gethostbyname_ex()
print (socket.gethostbyname_ex('localhost'))

# Test socket.gethostbyaddr()
