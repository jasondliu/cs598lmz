import socket
# Test socket.if_indextoname
if_indextoname = socket.if_indextoname(1)
assert if_indextoname == "lo0"
print("passed all tests..")
