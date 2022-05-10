import socket
# Test socket.if_indextoname
print(socket.if_indextoname(3))
print(socket.if_indextoname(7))
print(socket.if_indextoname(8))
print(socket.if_indextoname(9))
print(socket.if_indextoname(10))
# Test socket.if_indextoname with empty string
print(socket.if_indextoname(0))
# Test socket.if_indextoname with invalid index
try:
    print(socket.if_indextoname(999))
except OSError as err:
    print(err)
# Test socket.if_indextoname with not integer
try:
    print(socket.if_indextoname('lo'))
except TypeError as err:
    print(err)
# Test socket.if_indextoname with not integer
try:
    print(socket.if_indextoname(None))
except TypeError as err:
    print(err)
