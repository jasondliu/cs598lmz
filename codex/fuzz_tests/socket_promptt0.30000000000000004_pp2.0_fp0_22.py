import socket
# Test socket.if_indextoname()

if_indextoname = socket.if_indextoname

# Test invalid index
try:
    if_indextoname(-1)
except OSError as e:
    print(e)

# Test valid index
print(if_indextoname(1))
