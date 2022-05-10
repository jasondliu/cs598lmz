import socket
# Test socket.if_indextoname
try:
    socket.if_indextoname(1)
except socket.error as e:
    print('SKIP')
    raise SystemExit

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print(socket.if_indextoname(s.fileno()))
print(socket.if_indextoname(0))
print(socket.if_indextoname(1))
print(socket.if_indextoname(-1))
try:
    socket.if_indextoname(0x7fffffff)
except ValueError:
    print('ValueError')
