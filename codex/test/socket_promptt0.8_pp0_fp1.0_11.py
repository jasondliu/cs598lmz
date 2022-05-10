import socket
# Test socket.if_indextoname()
result = socket.if_indextoname(1)
if result != None:
    print("Error: if_indextoname(1) returned %s, not None" % result)
# Test socket.if_indextoname(0)
result = socket.if_indextoname(0)
if result != None:
    print("Error: if_indextoname(0) returned %s, not None" % result)
# Test socket.if_indextoname(socket.if_nametoindex("lo"))
result = socket.if_indextoname(socket.if_nametoindex("lo"))
if result != "lo":
    print("Error: if_indextoname(socket.if_nametoindex('lo')) returned %s, not 'lo'" % result)
# Test socket.if_indextoname(socket.if_nametoindex("eth0"))
