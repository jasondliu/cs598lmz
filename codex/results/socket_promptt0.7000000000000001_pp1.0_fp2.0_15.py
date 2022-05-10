import socket
# Test socket.if_indextoname in a common case.
socket.if_indextoname(1)

# Test socket.if_nameindex in a common case.
socket.if_nameindex()

# Test socket.if_nameindex in a non-common case.
socket.if_nameindex(1)

# Test socket.if_nameindex in an edge case.
socket.if_nameindex(0)

# Test socket.if_nameindex in an error case.
socket.if_nameindex(-1)
import socket
# Test socket.getnameinfo in a common case.
socket.getnameinfo(("", 0), 0xffff)

# Test socket.getnameinfo with a non-common flags case.
socket.getnameinfo(("", 0), 0xffff, 0xffff)

# Test socket.getnameinfo in an error case.
socket.getnameinfo(("", 0), 0xffff, 0xffff, 0xffff)
import socket
# Test socket.getaddrinfo in a common case.
socket.getaddrinfo("", 0)

# Test socket.getaddr
