import socket
# Test socket.if_indextoname()

for i in range(4, 10):
    try:
        print(i, socket.if_indextoname(i))
    except socket.error:
        pass
