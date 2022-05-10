import socket
socket.if_indextoname('3')

# 用于获取指定网络接口的索引
socket.if_nameindex()

# 用于获取本机所有网络接口的详细信息
socket.if_nameinfo(('127.0.0.1', 0))

# 用于获取本机网络接口的名称
socket.if_nametoindex('lo')

# 用于将数字地址转换成点分十进制
socket.inet_aton('127.0.0.1')

# 用于将点分十进制地址转换成数字
socket.inet_ntoa(b'\x7f
