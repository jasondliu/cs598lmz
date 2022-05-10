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

# 获取本地连接信息
psutil.net_connections(kind='inet4')

# 获取本地连接信息
psutil.net_connections(kind='inet6')

# 获取UNIX域套接字连接信息
psutil.
