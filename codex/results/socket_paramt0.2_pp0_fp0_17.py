import socket
socket.if_indextoname(3)

# 查看网络接口状态
import psutil
psutil.net_if_stats()

# 获取网络接口信息
psutil.net_if_addrs()

# 获取网络连接信息
psutil.net_connections()

# 获取当前网络连接信息
psutil.net_connections(kind='inet')

# 获取本机IP
import socket
socket.gethostbyname(socket.gethostname())

# 获取本机IPV4
socket.gethostbyname_ex(socket.gethostname())[2]

# 获取本机IPV6
socket.gethostbyname_ex(socket.gethostname())[3]

# 获取
