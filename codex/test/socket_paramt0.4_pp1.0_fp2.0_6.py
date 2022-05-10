import socket
socket.if_indextoname(3)

# 查看网卡状态
import psutil
print(psutil.net_if_stats())

# 查看网卡详细信息
import psutil
print(psutil.net_if_addrs())

# 查看网络连接信息
import psutil
print(psutil.net_connections())

# 查看网络接口状态
import psutil
print(psutil.net_if_stats())

# 获取网络接口信息
import psutil
print(psutil.net_if_addrs())

# 获取当前网络连接信息
import psutil
print(psutil.net_connections())

# 获取网络
