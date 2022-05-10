import socket
socket.if_indextoname(1)

socket.if_nameindex()

socket.if_nametoindex('Wi-Fi')

socket.socket(socket.AF_INET, socket.SOCK_STREAM).getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 4)

socket.socket(socket.AF_INET, socket.SOCK_STREAM).getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

socket.socket(socket.AF_INET, socket.SOCK_STREAM).getsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

socket.socket(socket.AF_INET, socket.SOCK_STREAM).getsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 0)

socket.socket(socket.AF_INET, socket.SOCK_STREAM).getsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)

