import socket
# Test socket.if_indextoname()
ifidx = socket.if_indextoname(2)
print(ifidx)

# Test socket.if_nametoindex()
ifname = socket.if_nametoindex('lo')
print(ifname)

# Test socket.if_nameindex()
ifnameidx = socket.if_nameindex()
print(ifnameidx)

# Test socket.if_nametoindex()
ifname = socket.if_nametoindex('lo')
print(ifname)

# Test socket.getservbyport()
service = socket.getservbyport(80)
print(service)

# Test socket.getservbyname()
port = socket.getservbyname('http')
print(port)

# Test socket.getnameinfo()
print(socket.getnameinfo(('127.0.0.1', 80), socket.NI_NUMERICHOST))
print(socket.getnameinfo(('127.0.0.1', 80), socket.NI_NUMERICSERV))
