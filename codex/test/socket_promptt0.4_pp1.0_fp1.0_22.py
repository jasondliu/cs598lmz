import socket
# Test socket.if_indextoname()

if_indextoname = socket.if_indextoname

for i in range(socket.if_nametoindex('lo'), socket.if_nametoindex('lo') + 5):
    try:
        print(i, if_indextoname(i))
    except OSError:
        pass
