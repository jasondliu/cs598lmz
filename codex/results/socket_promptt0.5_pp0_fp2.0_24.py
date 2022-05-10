import socket
# Test socket.if_indextoname
print socket.if_indextoname(1)
print socket.if_indextoname(2)
print socket.if_indextoname(3)
# Test socket.if_nameindex
for i in socket.if_nameindex():
    print i
# Test socket.if_nametoindex
print socket.if_nametoindex("lo")
print socket.if_nametoindex("wlan0")
print socket.if_nametoindex("eth0")
