import socket
# Test socket.if_indextoname
for i in range(0, 10):
    try:
        socket.if_indextoname(i)
    except ValueError:
        pass
