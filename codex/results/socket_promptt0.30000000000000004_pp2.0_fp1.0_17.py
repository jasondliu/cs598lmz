import socket
# Test socket.if_indextoname()

# The following tests are based on the interface names on my system.
# They may need to be changed if the interface names change.

# Test with valid interface index
print(socket.if_indextoname(3))

# Test with invalid interface index
try:
    print(socket.if_indextoname(100))
except ValueError:
    print("ValueError")

# Test with invalid type
try:
    print(socket.if_indextoname("3"))
except TypeError:
    print("TypeError")
