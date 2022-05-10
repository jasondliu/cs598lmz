import socket
# Test socket.if_indextoname()

# Test socket.if_indextoname() with valid index
index = socket.if_nametoindex('lo')
name = socket.if_indextoname(index)
print(name)

# Test socket.if_indextoname() with invalid index
try:
    socket.if_indextoname(0)
except ValueError:
    print("ValueError")

# Test socket.if_indextoname() with invalid type
