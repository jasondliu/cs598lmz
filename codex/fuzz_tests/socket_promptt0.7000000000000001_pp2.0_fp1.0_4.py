import socket
# Test socket.if_indextoname
print(socket.if_indextoname(1))
print(socket.if_indextoname(2))
print(socket.if_indextoname(4))
try:
    socket.if_indextoname(0)
except ValueError:
    print("ValueError")
try:
    socket.if_indextoname(5)
except ValueError:
    print("ValueError")

# Test socket.if_nameindex
print(socket.if_nameindex())

# Test socket.getfqdn
print(socket.getfqdn("8.8.8.8"))
# print(socket.getfqdn("localhost"))

# Test socket.getservbyport
print(socket.getservbyport(22))
print(socket.getservbyport(80))
print(socket.getservbyport(443))

# Test socket.gethostbyname
print(socket.gethostbyname("www.baidu.com"))
print(socket.gethostbyname("127.0.0.1"))

# Test
