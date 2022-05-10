import socket
# Test socket.if_indextoname()

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    print(s.if_indextoname(1))
    print(s.if_indextoname(1, 2))
    print(s.if_indextoname(1, 3))
