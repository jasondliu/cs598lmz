import socket
# Test socket.if_indextoname
print(socket.if_indextoname(1))
print(socket.if_indextoname(0xffffffff))

# Test socket.if_nameindex
print(socket.if_nameindex())

# Test socket.if_nameindex
print(socket.if_nametoindex("lo"))
print(socket.if_nametoindex("lo0"))
print(socket.if_nametoindex("eth0"))
print(socket.if_nametoindex("eth1"))
print(socket.if_nametoindex("eth2"))
print(socket.if_nametoindex("eth3"))
print(socket.if_nametoindex("eth4"))
print(socket.if_nametoindex("eth5"))
print(socket.if_nametoindex("eth6"))
print(socket.if_nametoindex("eth7"))
print(socket.if_nametoindex("eth8"))
print(socket.if_nametoindex("eth9"))
print(socket.if_nametoindex("eth10"))
print(socket.if_nametoindex("eth11
