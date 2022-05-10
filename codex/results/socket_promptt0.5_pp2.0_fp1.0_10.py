import socket
# Test socket.if_indextoname()
for i in range(256):
    try:
        print("%d: %s" % (i, socket.if_indextoname(i)))
    except:
        pass
