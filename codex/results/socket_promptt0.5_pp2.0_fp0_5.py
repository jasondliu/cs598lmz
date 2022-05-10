import socket
# Test socket.if_indextoname()
try:
    socket.if_indextoname(1)
except OSError as e:
    print("SKIP")
    raise SystemExit

# Test socket.if_nametoindex()
try:
    socket.if_nametoindex("lo")
except OSError as e:
    print("SKIP")
    raise SystemExit

# Test socket.if_nameindex()
try:
    socket.if_nameindex()
except OSError as e:
    print("SKIP")
    raise SystemExit

import uos
print(uos.if_indextoname(1))
print(uos.if_nametoindex("lo"))
print(uos.if_nameindex())
