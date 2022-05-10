import socket
# Test socket.if_indextoname()
print(socket.if_indextoname(1))
print(socket.if_indextoname(0))

# Test socket.if_nameindex()
print(socket.if_nameindex())

# Test socket.if_nametoindex()
print(socket.if_nametoindex("en0"))
print(socket.if_nametoindex("lo0"))

# Test socket.gethostbyname()
print(socket.gethostbyname("www.python.org"))

# Test socket.gethostbyname_ex()
print(socket.gethostbyname_ex("www.python.org"))

# Test socket.gethostbyaddr()
print(socket.gethostbyaddr("151.101.44.223"))

# Test socket.gethostname()
print(socket.gethostname())

# Test socket.getfqdn()
print(socket.getfqdn("www.baidu.com"))

# Test socket.getaddrinfo()
print(socket.getaddrinfo("www.python.org", 80))

#
