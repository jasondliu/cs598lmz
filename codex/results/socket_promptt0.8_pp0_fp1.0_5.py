import socket
# Test socket.if_indextoname(1)
print(socket.if_indextoname(1))
if socket.if_indextoname(1) != None:
    print("1")
else:
    print("0")
# Test socket.if_nametoindex("lo")
print(socket.if_nametoindex("lo"))
if socket.if_nametoindex("lo") != None:
    print("1")
else:
    print("0")
