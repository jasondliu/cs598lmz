import socket
# Test socket.if_indextoname()

if_indextoname = socket.if_indextoname

print if_indextoname(0)
for i in range(1,10):
    print if_indextoname(i)
