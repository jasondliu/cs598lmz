import socket
# Test socket.if_indextoname

# TODO: Test with a real interface

result = socket.if_indextoname(1)
print(result)

# No interface with index 0
try:
    socket.if_indextoname(0)
except ValueError as e:
    print(e)
