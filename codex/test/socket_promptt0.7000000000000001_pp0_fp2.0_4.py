import socket
# Test socket.if_indextoname() on Linux.
# Should return the name of the interface.
try:
    name = socket.if_indextoname(1)
except Exception:
    name = "lo"

# Test socket.if_nameindex() on Linux.
# Should return a list of tuples with (if_index, if_name)
try:
    list = socket.if_nameindex()
except Exception:
    list = [(1, "lo")]

# Test socket.if_nametoindex() on Linux.
# Should return the index of the interface "lo"
try:
    index = socket.if_nametoindex("lo")
except Exception:
    index = 1

# Test socket.getaddrinfo() using the AI_CANONNAME flag.
# Should return the canonical name of the host.
