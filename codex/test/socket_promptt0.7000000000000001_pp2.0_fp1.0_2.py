import socket
# Test socket.if_indextoname()
print("\nsocket.if_indextoname()")

for i in range(0,10):
    try:
        print("i = %d, name = %s" % (i, socket.if_indextoname(i)))
    except:
        print("i = %d, name = <NULL>" % i)
# Test socket.if_nameindex()
print("\nsocket.if_nameindex()")

for i in range(0,10):
    try:
        print("i = %d, name = %s" % (i, socket.if_nameindex(i)))
    except:
        print("i = %d, name = <NULL>" % i)
# Test socket.if_nameindex()
print("\nsocket.if_nameindex()")

for i in range(0,10):
    try:
        print("i = %d, name = %s" % (i, socket.if_nameindex(i)))
    except:
        print("i = %d, name = <NULL>" % i)
#
