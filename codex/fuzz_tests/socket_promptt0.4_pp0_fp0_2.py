import socket
# Test socket.if_indextoname
if_indextoname = socket.if_indextoname(1)
print(if_indextoname)

# Test socket.if_nameindex
if_nameindex = socket.if_nameindex()
print(if_nameindex)

# Test socket.if_nametoindex
if_nametoindex = socket.if_nametoindex(if_indextoname)
print(if_nametoindex)
