import socket
# Test socket.if_indextoname
# On Windows, "the argument to if_indextoname is a network interface index"
# On Linux, "the argument to if_indextoname is an interface name"

s = socket.socket()
count = socket.if_nameindex()
assert count is not None  # the returned array is empty if there are no network interfaces

index = count[0][0]
# if_indextoname is not supported on Windows
name = None
try:
    name = socket.if_indextoname(index)
    assert type(name) == str
except (NameError, socket.error):
    pass

# if_indextoname is not supported on Linux
index2 = None
try:
    index2 = socket.if_nametoindex(name)
    assert i
