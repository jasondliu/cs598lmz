import socket
# Test socket.if_indextoname()
assert socket.if_indextoname(1) == "lo"
# Test socket.if_nametoindex()
assert socket.if_nametoindex("lo") == 1

print("passed all tests..")
