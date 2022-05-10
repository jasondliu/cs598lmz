import socket
socket.if_indextoname(4)

# 使用网络接口的索引获取网络接口的名称，返回的是一个字节串
# socket.if_nameindex()
# 使用网络接口名称获取网络接口的索引，返回的是一个元组
socket.if_nametoindex('lo')

# 获取网络接口的详细信息，返回的是一个元组
socket.if_nameinfo(('192.168.0.1', 80))
socket.if_nameinfo(('192.168.0.1', 80, 0, 0))

# 获取本地的网
