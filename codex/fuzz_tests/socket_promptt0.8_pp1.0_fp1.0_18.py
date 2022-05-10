import socket
# Test socket.if_indextoname()
import socket

result = socket.if_indextoname(1)
print(result)

result = socket.if_indextoname(100)
print(result)

result = socket.if_indextoname(4)
print(result)

result = socket.if_indextoname(3)
print(result)

result = socket.if_indextoname(5)
print(result)

result = socket.if_indextoname(2)
print(result)


# Test socket.if_nameindex()
import socket

result = socket.if_nameindex()
print(result)
