import socket
# Test socket.if_indextoname()
try:
    socket.if_indextoname(0)
except OSError as e:
    if e.errno != errno.EINVAL:
        raise
    print("SKIP")
    raise SystemExit

# Test socket.if_indextoname() with invalid index
try:
    socket.if_indextoname(65536)
except OSError as e:
    if e.errno != errno.EINVAL:
        raise
    print("SKIP")
    raise SystemExit

# Test socket.if_nametoindex()
try:
    socket.if_nametoindex("lo")
except OSError as e:
    if e.errno != errno.ENODEV:
        raise
    print("SKIP")
    raise SystemExit

# Test socket.if_nametoindex() with invalid index
try:
    socket.if_nametoindex("")
except OSError as e:
    if e.errno != errno.ENODEV:
        raise
    print("SK
