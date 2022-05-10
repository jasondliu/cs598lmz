import socket
socket.if_indextoname(3)

# 查看某个接口的状态
import psutil
psutil.net_if_stats()['lo']

# 获取某个接口的IP地址
import psutil
psutil.net_if_addrs()['lo']

# 获取网络连接信息
import psutil
psutil.net_connections()

# 获取网络接口状态
import psutil
psutil.net_if_stats()

# 获取网络接口信息
import psutil
psutil.net_if_addrs()

# 获取网络连接信息
import psutil
psutil.net_connections()

# 获取网络连
