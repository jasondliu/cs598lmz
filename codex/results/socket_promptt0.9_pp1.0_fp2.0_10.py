import socket
# Test socket.if_indextoname()
#

lst = socket.if_indextoname(1)
print(lst)
lst = socket.if_indextoname(15)
print(lst)
