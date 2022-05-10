import socket
# Test socket.if_indextoname
print(socket.if_indextoname(1))
# Test socket.if_nameindex
nameindex = socket.if_nameindex()
for index, name in nameindex:
    print(index, name)
# Test socket.if_nameindex
nameindex = socket.if_nametoindex('lo')
print(nameindex)
# Test socket.getaddrinfo
addrinfo = socket.getaddrinfo(socket.gethostname(), None, 0, 0, socket.IPPROTO_TCP)
for addr in addrinfo:
    print(addr)
# Test socket.getnameinfo
nameinfo = socket.getnameinfo(addr[4], socket.NI_NUMERICHOST)
print(nameinfo)
# Test socket.getaddrinfo
addrinfo = socket.getaddrinfo('127.0.0.1', 80, 0, 0, socket.IPPROTO_TCP)
for addr in addrinfo:
    print(addr)
# Test socket.gethostbyname
hostbyname = socket.gethostbyname(socket.gethostname())
