import socket
# Test socket.if_indextoname()

for i in range(128):
    try:
        print(socket.if_indextoname(i))
    except:
        pass
