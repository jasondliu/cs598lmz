import socket
socket.if_indextoname(16)

print("""Attempting to bind to 16 (DOT11MESH) with type 0""")
socket.bind_or_die(16, 0)

print("""Attempting to bind to 32 (LOOPBACK) with type 0""")
try: 
    socket.bind_or_die(32, 0)
excep
