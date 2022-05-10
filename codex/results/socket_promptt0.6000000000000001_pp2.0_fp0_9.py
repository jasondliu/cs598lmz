import socket
# Test socket.if_indextoname(3)
try:
    socket.if_indextoname(0)
except OSError:
    pass
else:
    assert 0, "should raise OSError"

try:
    socket.if_indextoname(0xffffffff)
except OSError:
    pass
else:
    assert 0, "should raise OSError"

# Test socket.if_nameindex(3)
if_nameindex = socket.if_nameindex()
for (index, name) in if_nameindex:
    socket.if_indextoname(index) == name

for (index, name) in if_nameindex:
    socket.if_nametoindex(name) == index

# Test socket.if_freenameindex(3)
socket.if_freenameindex(if_nameindex)

# Test socket.if_nameindex(3) with invalid input
import _socket
# This should raise a ValueError
try:
    _socket.if_nameindex(b"")
except ValueError:
    pass
