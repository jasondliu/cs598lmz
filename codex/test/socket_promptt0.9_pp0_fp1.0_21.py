import socket
# Test socket.if_indextoname()
print(socket.if_indextoname(2))
# Test socket.if_nameindex()
# tuple list: [(1, 'lo'), (2, 'p1p1'), (3, 'p1p2'), (4, 'p1p3'), (5, 'p1p4')]
print(socket.if_nameindex())
# Test socket.if_nameinfo()
# (addr1, 0) format
# ('127.0.0.1', 0)
print(socket.if_nameinfo(('127.0.0.1', 80)))
# (addr1, port) format
# ('127.0.0.1', 80)
print(socket.if_nameinfo((('127.0.0.1', 80), 0)))
# (addr1, port, flow_info, scope_id) format
# ('127.0.0.1', 80)
print(socket.if_nameinfo((('127.0.0.1', 80, 0, 0))))
# Test socket.getaddrinfo() - Address information translation
