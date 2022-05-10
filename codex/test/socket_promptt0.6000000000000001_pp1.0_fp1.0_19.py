import socket
# Test socket.if_indextoname() and socket.if_nametoindex()

try:
    socket.if_indextoname(1)
except OSError as e:
    print(e.errno, e.strerror)
    # Tested on linux, the result is:
    # 19 No such device


try:
    socket.if_nametoindex('lo')
except OSError as e:
    print(e.errno, e.strerror)
    # Tested on linux, the result is:
    # 19 No such device
