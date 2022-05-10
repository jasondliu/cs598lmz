import socket
# Test socket.if_indextoname()
print(socket.if_indextoname(1))
print(socket.if_indextoname(2))

# Test socket.if_nameindex()
for i in socket.if_nameindex():
    print(i)

# Test socket.if_nametoindex()
print(socket.if_nametoindex('lo'))
print(socket.if_nametoindex('eth0'))

# Test socket.gethostbyname()
print(socket.gethostbyname('localhost'))
print(socket.gethostbyname('www.python.org'))

# Test socket.gethostbyname_ex()
print(socket.gethostbyname_ex('localhost'))
print(socket.gethostbyname_ex('www.python.org'))

# Test socket.gethostname()
print(socket.gethostname())

# Test socket.gethostbyaddr()
print(socket.gethostbyaddr('127.0.0.1'))

# Test socket.getnameinfo()
print(socket.getnameinfo(('
