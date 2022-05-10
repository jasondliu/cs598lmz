import socket
socket.if_indextoname(s.getsockopt(socket.SOL_SOCKET, socket.SO_BINDTODEVICE))
s.shutdown(socket.SHUT_RDWR)
s.close()
