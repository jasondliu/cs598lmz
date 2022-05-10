import socket
# Test socket.if_indextoname()
#
# 1. if_indextoname() raises OSError if the interface index is not valid
# 2. if_indextoname() returns the interface name as a string
#
print("Test socket.if_indextoname()")
try:
    socket.if_indextoname(-1)
except OSError as e:
    print("1. PASSED")
else:
    print("1. FAILED")

r = socket.if_indextoname(0)
print(r, type(r))
if isinstance(r, str):
    print("2. PASSED")
else:
    print("2. FAILED")
