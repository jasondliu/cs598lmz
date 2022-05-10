import socket
socket.if_indextoname(1)

socket.if_nameindex()

# 获得一个套接字 **绑定** 到主机和端口
sock = socket.socket()

sock.bind(('',8080))
