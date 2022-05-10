import socket
# Test socket.if_indextoname()

for i in range(100):
    try:
        socket.if_indextoname(i)
    except OSError:
        pass
    else:
        print(i, socket.if_indextoname(i))
