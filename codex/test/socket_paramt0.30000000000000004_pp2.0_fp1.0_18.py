import socket
socket.if_indextoname(3)

# 查看网卡的状态
import psutil
psutil.net_if_stats()

# 获取网卡的详细信息
psutil.net_if_addrs()

# 获取网络连接信息
psutil.net_connections()

# 获取网络接口流量
psutil.net_io_counters()

# 获取网络接口流量(每个网卡的)
psutil.net_io_counters(pernic=True)

# 获取网卡的状态
psutil.net_if_stats()

# 获取网卡的详细信息
psutil.net_if_addrs()
