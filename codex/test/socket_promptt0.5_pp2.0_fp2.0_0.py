import socket
# Test socket.if_indextoname()
for i in range(0, 8):
    try:
        print("%2d: %s" % (i, socket.if_indextoname(i)))
    except:
        pass

# Test socket.if_nameindex()
for i in socket.if_nameindex():
    print("%2d: %s" % i)

# Test socket.if_nametoindex()
for i in range(0, 8):
    try:
        print("%2d: %s" % (i, socket.if_nametoindex(socket.if_indextoname(i))))
    except:
        pass
