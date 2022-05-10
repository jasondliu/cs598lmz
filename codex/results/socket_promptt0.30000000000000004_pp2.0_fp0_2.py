import socket
# Test socket.if_indextoname()

# Test with invalid index
try:
    socket.if_indextoname(-1)
except ValueError:
    print("ValueError")

# Test with valid index
try:
    socket.if_indextoname(1)
except ValueError:
    print("ValueError")

# Test with invalid index
try:
    socket.if_indextoname(0)
except ValueError:
    print("ValueError")
