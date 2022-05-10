import socket
# Test socket.if_indextoname()
print(socket.if_indextoname(2))
print(socket.if_indextoname(9))

# Test socket.if_nametoindex()
print(socket.if_nametoindex('lo'))
print(socket.if_nametoindex('eth0'))
print(socket.if_nametoindex('wlan0'))

# Test socket.gethostbyname()
print(socket.gethostbyname('127.0.0.1'))
print(socket.gethostbyname('localhost'))

# Test socket.gethostbyaddr()
print(socket.gethostbyaddr('127.0.0.1'))
print(socket.gethostbyaddr('localhost'))
print(socket.gethostbyaddr('192.168.1.1'))
print(socket.gethostbyaddr('wlan0'))

# Test socket.gethostname()
print(socket.gethostname())

# Test socket.gethostbyname_ex()
print(socket.gethostbyname_ex('127.0.0
