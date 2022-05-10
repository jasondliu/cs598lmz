import socket
# Test socket.if_indextoname()
try:
    socket.if_indextoname(0)
except:
    print("SKIP")
    raise SystemExit

# Test invalid argument
try:
    socket.if_indextoname(1)
except OSError as e:
    print(e.args[0] == errno.EINVAL)

# Test invalid argument
try:
    socket.if_indextoname(0, "")
except TypeError:
    print("SKIP")
    raise SystemExit

# Test valid argument
print(socket.if_indextoname(0) == "lo")
