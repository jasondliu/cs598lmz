import socket
# Test socket.if_indextoname
print(socket.if_indextoname(7))
print(socket.if_indextoname(165))
print(
    socket.if_indextoname(
        165))  # Testing with int converted to larger variable size
print(socket.if_indextoname(99999999999999999999999999999))

# Test socket.if_nametoindex
print(socket.if_nametoindex("lo"))
print(socket.if_nametoindex("enp94s0f1"))
print(socket.if_nametoindex("ethernet"))
try:
    print(socket.if_nametoindex("loopback-"))
except ValueError as e:
    print("Ethernet interface not found.")
print(socket.if_nametoindex("enp9s0f1"))

print(
    socket.if_nametoindex("enp9s0f1"))  # Testing with int converted to larger variable size

try:
    print(socket.if_nametoindex("socket"))
except socket.error as e:
    print("Socket interface
