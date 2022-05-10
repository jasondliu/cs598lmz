import socket
# Test socket.if_indextoname()
print socket.if_indextoname(3)
print socket.if_indextoname(socket.if_nametoindex('lo'))
print socket.if_indextoname('1')
print socket.if_indextoname(1L)
try:
    print socket.if_indextoname(-1)
except ValueError:
    print "ValueError"
try:
    print socket.if_indextoname(1000000000)
except ValueError:
    print "ValueError"
try:
    print socket.if_indextoname(1.0)
except ValueError:
    print "ValueError"

# Test socket.if_nameindex()
print socket.if_nameindex()

# Test socket.if_nameindex()
print socket.if_nameindex()
