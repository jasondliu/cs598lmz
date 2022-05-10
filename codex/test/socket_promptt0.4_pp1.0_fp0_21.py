import socket
# Test socket.if_indextoname
try:
    socket.if_indextoname(0)
except socket.error as e:
    if e.errno == errno.ENODEV:
        print("SKIP")
        raise SystemExit

# Test socket.if_indextoname
print(socket.if_indextoname(0))

# Test socket.if_nametoindex
print(socket.if_nametoindex("lo"))

# Test socket.if_nametoindex
try:
    socket.if_nametoindex("bad_interface")
except socket.error as e:
    if e.errno == errno.ENODEV:
        print("bad_interface")
    else:
        raise

# Test socket.if_nametoindex
try:
    socket.if_nametoindex(b"bad_interface")
except socket.error as e:
    if e.errno == errno.ENODEV:
        print("bad_interface")
    else:
        raise

# Test socket.if_nametoindex
