import socket
# Test socket.if_indextoname
print(socket.if_indextoname(1))
"lo"

# Test socket.if_nameindex
print(socket.if_nameindex())
[(1, b'lo')]

# Test socket.if_nametoindex
print(socket.if_nametoindex(b"lo"))
1

# Test socket.if_nameindex
socket.getnameinfo(bytes(), 0)
(b'', b'')
socket.getnameinfo(bytes(), 0, 0)
(b'', b'', 0, 0)

# Test socket.getnameinfo


# Test socket.getaddrinfo
print([sockaddr for _, sockaddr in socket.getaddrinfo(b"localhost", None, 0,
                                                      socket.SOCK_STREAM,
                                                      socket.SOL_SOCKET,
                                                      0)])
[(2, 1, 6, '', ('127.0.0.1', 0))]
[(2, 2, 17, '', ('127.0.0.1', 0))]
[(
