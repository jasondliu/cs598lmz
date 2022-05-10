import socket
# Test socket.if_indextoname
print(socket.if_indextoname(0))
# 2 of 5
print(socket.if_indextoname(1))
print(socket.if_indextoname(2))
# 3 of 5
print(socket.if_indextoname(3))
print(socket.if_indextoname(4))
# 4 of 5
print(socket.if_indextoname(5))
print(socket.if_indextoname(6))
# 5 of 5
print(socket.if_indextoname(7))
print(socket.if_indextoname(8))

# End of test for socket.if_indextoname

# Test socket.if_indextoname with invalid args
print(socket.if_indextoname(-1))
print(socket.if_indextoname(9))
