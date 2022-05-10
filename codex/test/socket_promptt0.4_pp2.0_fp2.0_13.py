import socket
# Test socket.if_indextoname()
try:
    socket.if_indextoname(1)
except:
    print("SKIP")
    raise SystemExit

try:
    socket.if_indextoname(1, "foo")
except TypeError:
    print("TypeError")

try:
    socket.if_indextoname(1, "foo", "bar")
except TypeError:
    print("TypeError")

try:
    socket.if_indextoname(1, "foo", "bar", "baz")
except TypeError:
    print("TypeError")

try:
    socket.if_indextoname(1, "foo", "bar", "baz", "quux")
except TypeError:
    print("TypeError")
