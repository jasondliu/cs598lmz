import socket
socket.if_indextoname(2)

# 1.4 获取本地ip地址
print(socket.gethostbyname(socket.gethostname()))
