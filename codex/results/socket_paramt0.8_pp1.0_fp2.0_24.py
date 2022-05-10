import socket
socket.if_indextoname(1)
print(socket.if_indextoname(1))
socket.if_nameindex()
print (socket.if_nameindex())

# $ python3 socket_if_nameindex.py
# en0
# [(1, 'lo0'), (2, 'gif0'), (3, 'stf0'), (4, 'en0'), (5, 'en1'), (6, 'fw0'), (7, 'vmnet1'), (8, 'vmnet8')]
