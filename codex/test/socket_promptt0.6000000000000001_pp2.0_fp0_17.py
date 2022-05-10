import socket
# Test socket.if_indextoname() with a valid interface name.
for i in range(socket.if_nametoindex('lo'), socket.if_nametoindex('lo') + 16):
    try:
        socket.if_indextoname(i)
    except OSError as e:
        print(e.errno)
