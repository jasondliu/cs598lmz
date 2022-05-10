import socket
# Test socket.if_indextoname
print(socket.if_indextoname(1))
print(socket.if_indextoname(5))

try:
    print(socket.if_indextoname(1000))
except ValueError:
    print("ValueError")

# Test socket.if_nametoindex
print(socket.if_nametoindex("lo"))
print(socket.if_nametoindex("eth0"))

try:
    print(socket.if_nametoindex("ipython"))
except ValueError:
    print("ValueError")
