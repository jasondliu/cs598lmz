import socket
# Test socket.if_indextoname() with an invalid index.

# Get the interface name to test with
ifname = socket.if_indextoname(1)

# Test with an invalid index (0)
try:
    socket.if_indextoname(0)
except ValueError as e:
    print('Got expected exception:', e)

# Test with an invalid index (negative)
try:
    socket.if_indextoname(-1)
except ValueError as e:
    print('Got expected exception:', e)

# Test with an invalid index (too large)
try:
    socket.if_indextoname(sys.maxsize)
except ValueError as e:
    print('Got expected exception:', e)
