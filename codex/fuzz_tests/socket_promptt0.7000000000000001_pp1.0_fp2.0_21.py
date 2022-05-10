import socket
# Test socket.if_indextoname() and socket.if_nametoindex() functions

# Check the error handling
try:
    socket.if_indextoname(-1)
except OSError:
    pass
else:
    print("OSError not raised")
try:
    socket.if_nametoindex("no-such-interface")
except OSError:
    pass
else:
    print("OSError not raised")

# Check that each call is the inverse of the other
for i in range(socket.if_nametoindex("lo0"),
               socket.if_nametoindex("lo0") + 10):
    i2n = socket.if_indextoname(i)
    n2i = socket.if_nametoindex(i2n)
    if i != n2i:
        print("%s != %d" % (n2i, i))
    if i2n != socket.if_indextoname(n2i):
        print("%s != %s" % (i2n, socket.if_indextoname(n2i)))
