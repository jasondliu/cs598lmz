import socket
# Test socket.if_indextoname()
print(socket.if_indextoname(1))
print(socket.if_indextoname(2))
print(socket.if_indextoname(3))

# Test socket.if_indextoname()
print(socket.if_nametoindex('lo'))
print(socket.if_nametoindex('eth0'))
print(socket.if_nametoindex('wlan0'))

# Test socket.if_nameindex()
print(socket.if_nameindex())

# Test socket.if_nameindex()
print(socket.gethostbyname('localhost'))
print(socket.gethostbyname('google.com'))

# Test socket.gethostbyname_ex()
print(socket.gethostbyname_ex('localhost'))
print(socket.gethostbyname_ex('google.com'))

# Test socket.gethostbyaddr()
print(socket.gethostbyaddr('127.0.0.1'))

# Test socket.gethostname()
print(socket.gethostname())
