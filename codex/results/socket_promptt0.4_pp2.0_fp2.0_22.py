import socket
# Test socket.if_indextoname
try:
    socket.if_indextoname(1)
except Exception as e:
    print(e)

# Test socket.if_nameindex
try:
    socket.if_nameindex()
except Exception as e:
    print(e)

# Test socket.if_nametoindex
try:
    socket.if_nametoindex("lo")
except Exception as e:
    print(e)
