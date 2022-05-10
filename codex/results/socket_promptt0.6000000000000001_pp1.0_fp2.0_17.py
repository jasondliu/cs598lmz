import socket
# Test socket.if_indextoname

# Test socket.if_indextoname with invalid index
try:
    socket.if_indextoname(-1)
except ValueError:
    print("Correctly raised ValueError with invalid index")
else:
    print("Failed to raise ValueError with invalid index")

# Test socket.if_indextoname with valid index
name = socket.if_indextoname(1)
print("Index 1 is", name)
print(socket.if_indextoname(socket.if_nametoindex(name)))

# Test socket.if_indextoname with bad index
try:
    socket.if_indextoname(9999)
except ValueError:
    print("Correctly raised ValueError with invalid index")
else:
    print("Failed to raise ValueError with invalid index")
