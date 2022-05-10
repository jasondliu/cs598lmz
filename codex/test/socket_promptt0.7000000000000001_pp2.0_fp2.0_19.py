import socket
# Test socket.if_indextoname
print(socket.if_indextoname(1))

try:
    print(socket.if_indextoname(0))
except OSError:
    print("OSError")

print(socket.if_indextoname(None))

try:
    print(socket.if_indextoname(-1))
except ValueError:
    print("ValueError")

try:
    print(socket.if_indextoname(0xffffffff))
except ValueError:
    print("ValueError")

# Test socket.if_nameindex()
print([x for x in socket.if_nameindex()])

# Test socket.if_nametoindex()
socket.if_nametoindex('lo')

try:
    socket.if_nametoindex('lo0')
except OSError:
    print("OSError")

try:
    socket.if_nametoindex('')
except OSError:
    print("OSError")

