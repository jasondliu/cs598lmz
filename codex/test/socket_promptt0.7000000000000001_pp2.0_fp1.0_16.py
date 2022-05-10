import socket
# Test socket.if_indextoname function
print(socket.if_indextoname(3))
print(socket.if_indextoname(4))
print(socket.if_indextoname(2))

# Test socket.if_nametoindex function
print(socket.if_nametoindex("eth0"))
print(socket.if_nametoindex("eth1"))
print(socket.if_nametoindex("lo"))

# Test socket.gethostbyaddr function
print(socket.gethostbyaddr("127.0.0.1"))

# Test socket.gethostbyname function
print(socket.gethostbyname("www.baidu.com"))
print(socket.gethostbyname("www.google.com"))

# Test socket.gethostname function
print(socket.gethostname())

# Test socket.getprotobyname function
print(socket.getprotobyname("tcp"))
print(socket.getprotobyname("udp"))

# Test socket.getservbyname function
print(socket.getservbyname("http"))
