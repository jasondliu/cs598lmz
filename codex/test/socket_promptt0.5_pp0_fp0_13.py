import socket
# Test socket.if_indextoname()
print(socket.if_indextoname(1))

# Test socket.if_nameindex()
print(socket.if_nameindex())

# Test socket.if_nametoindex()
print(socket.if_nametoindex('eth0'))

# Test socket.getaddrinfo()
print(socket.getaddrinfo('www.baidu.com', 80, 0, 0, socket.IPPROTO_TCP))

# Test socket.gethostbyname()
print(socket.gethostbyname('www.baidu.com'))

# Test socket.gethostbyname_ex()
print(socket.gethostbyname_ex('www.baidu.com'))

# Test socket.gethostname()
print(socket.gethostname())

# Test socket.gethostbyaddr()
print(socket.gethostbyaddr('192.168.1.1'))

# Test socket.getnameinfo()
print(socket.getnameinfo(('192.168.1.1', 80), 0))

# Test socket
