import socket
# Test socket.if_indextoname()
print(socket.if_indextoname(1))

# Test socket.if_nameindex()
print(socket.if_nameindex())

# Test socket.if_nametoindex()
print(socket.if_nametoindex('lo'))

# Test socket.getaddrinfo()
print(socket.getaddrinfo('www.baidu.com', 80))

# Test socket.gethostbyname()
print(socket.gethostbyname('www.baidu.com'))

# Test socket.gethostbyname_ex()
print(socket.gethostbyname_ex('www.baidu.com'))

# Test socket.gethostname()
print(socket.gethostname())

# Test socket.getnameinfo()
print(socket.getnameinfo(('127.0.0.1', 80), 0))

# Test socket.getprotobyname()
print(socket.getprotobyname('tcp'))

# Test socket.getservbyname()
print(socket.getservbyname('http
