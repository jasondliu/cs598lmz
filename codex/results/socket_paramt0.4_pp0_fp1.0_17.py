import socket
socket.if_indextoname(3)

# 获取接口索引
socket.if_nametoindex('en0')

# 获取接口地址
socket.if_nameindex()

# 获取本地接口信息
socket.if_nameindex()

# 获取接口信息
socket.if_nameinfo(sockaddr, flags)

# 获取本机名
socket.gethostname()

# 获取本机地址
socket.gethostbyname(hostname)

# 获取本机地址列表
socket.gethostbyname_ex(hostname)

# 获取本机IP地址
socket.gethostbyname(socket.gethostname())

# 获取本机IP地址列
