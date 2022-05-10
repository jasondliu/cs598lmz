import socket
# Test socket.if_indextoname
# I got "eth0", and on Windows it is "lo"
print(socket.if_indextoname(1))
# Test socket.if_indextoname
# I got {'enp7s0': 3, 'lo': 1}, and on Windows, it is {}
print(socket.if_nameindex())
# Test socket.if_nametoindex
# I got 1, and on Windows, it is 1
print(socket.if_nametoindex('enp7s0'))
