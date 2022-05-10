import socket
# Test socket.if_indextoname()
ip = socket.inet_aton('172.16.12.13')
print(socket.if_indextoname(150))  # enp8s0f1
print(socket.if_indextoname(151))  # enp0s31f6
print(socket.if_indextoname(255))  # No such device
print(socket.if_indextoname(150), ip)
