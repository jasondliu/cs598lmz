import socket
# Test socket.if_indextoname()

print(socket.if_indextoname(1))
print(socket.if_indextoname(1, 'eth'))

try:
    print(socket.if_indextoname(1, 'lo'))
except OSError as e:
    print(e)

try:
    print(socket.if_indextoname(1, 'lo0'))
except OSError as e:
    print(e)

try:
    print(socket.if_indextoname(1, 'lo1'))
except OSError as e:
    print(e)

try:
    print(socket.if_indextoname(1, 'lo2'))
except OSError as e:
    print(e)

try:
    print(socket.if_indextoname(1, 'lo3'))
except OSError as e:
    print(e)
