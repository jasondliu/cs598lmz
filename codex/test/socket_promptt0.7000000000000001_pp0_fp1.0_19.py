import socket
# Test socket.if_indextoname()
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BINDTODEVICE, 'en0' + chr(0))
print(s.getsockname())
