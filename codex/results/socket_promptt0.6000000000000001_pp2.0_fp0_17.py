import socket
# Test socket.if_indextoname() with a valid interface name.
for i in range(socket.if_nametoindex('lo'), socket.if_nametoindex('lo') + 16):
    try:
        socket.if_indextoname(i)
    except OSError as e:
        print(e.errno)
        if e.errno != errno.ENXIO:
            raise e

# Test socket.if_indextoname() with an invalid interface name.
for i in range(socket.if_nametoindex('lo') - 1, socket.if_nametoindex('lo') - 16, -1):
    try:
        socket.if_indextoname(i)
    except OSError as e:
        print(e.errno)
        if e.errno != errno.ENXIO:
            raise e
