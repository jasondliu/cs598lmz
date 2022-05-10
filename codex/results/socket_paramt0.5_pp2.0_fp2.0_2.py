import socket
socket.if_indextoname(1)

# 从网络接口的名字获取网络接口的索引
socket.if_nametoindex('eth0')

# 获取本机的所有网络接口名
socket.if_nameindex()

# 获取本机的所有网络接口信息
socket.if_nametoindex()

# 获取本机的IP地址
socket.gethostbyname(socket.gethostname())

# 获取本机的所有网络接口的IP地址
socket.gethostbyname_ex(socket.gethostname())

# 查询域名的IP地址
socket.gethostbyname('www.python.org
