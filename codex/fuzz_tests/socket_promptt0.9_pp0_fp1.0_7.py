import socket
# Test socket.if_indextoname()

for i in range(100):
    name  = socket.if_indextoname(i)
    print '%d\t=> "%s"' % (i, name)
