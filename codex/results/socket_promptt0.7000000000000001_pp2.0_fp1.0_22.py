import socket
# Test socket.if_indextoname()
for i in range(0, 10):
    try:
        print i, socket.if_indextoname(i)
    except (IOError, OSError):
        print i, 'None'

print
# Test socket.if_nameindex()
for i in socket.if_nameindex():
    print i
