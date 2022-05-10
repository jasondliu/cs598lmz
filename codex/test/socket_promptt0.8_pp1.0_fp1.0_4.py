import socket
# Test socket.if_indextoname()
print(socket.if_indextoname(3))
# socket.if_indextoname(1) # raises NotImplementedError on Linux, Win
print(socket.if_indextoname(0))
print(socket.if_indextoname(-1))
print(socket.if_indextoname(0xffffffff))
