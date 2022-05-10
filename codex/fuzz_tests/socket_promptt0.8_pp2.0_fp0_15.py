import socket
# Test socket.if_indextoname()
host = socket.gethostname()
print("Host name: %s" % host)
for i in range(255):
    name = socket.if_indextoname(i)
    if name is not None:
        print("Index %d: %s" % (i, name))
