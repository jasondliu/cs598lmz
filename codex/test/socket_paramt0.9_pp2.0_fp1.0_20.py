import socket
socket.if_indextoname(16)

print("""Attempting to bind to 16 (DOT11MESH) with type 0""")
socket.bind_or_die(16, 0)

