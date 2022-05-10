import socket
# Test socket.if_indextoname()
socket.if_indextoname(0)
# Test socket.if_nametoindex()
socket.if_nametoindex("lo0")

print("test_socket: OK")
