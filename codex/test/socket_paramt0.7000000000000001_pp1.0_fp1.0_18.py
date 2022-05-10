import socket
socket.if_indextoname(1)

print(socket.gethostbyaddr('127.0.0.1'))
print(socket.gethostbyname('localhost'))
print(socket.gethostname())

print(socket.gethostbyname_ex('localhost'))

print(socket.gethostbyname_ex('localhost')[2])

print(socket.gethostbyname_ex('localhost')[2][0])
