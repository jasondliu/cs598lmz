import socket
socket.if_indextoname(3)

# 获取网卡的索引
socket.if_nameindex()

# 获取网卡的信息
socket.if_nametoindex('eth0')

# 获取网卡的信息
socket.if_nameinfo(('127.0.0.1', 80))

# 获取网卡的信息
socket.if_nameinfo(('127.0.0.1', 80), 0)

# 获取网卡的信息
socket.if_nameinfo(('127.0.0.1', 80), 1)

# 获取网卡的信息
socket.if_nameinfo(('127.0.0.1', 80), 2)

