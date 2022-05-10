import socket
socket.if_indextoname(1)

# 查看网卡状态
import psutil
psutil.net_if_stats()

# 查看网卡详细信息
psutil.net_if_addrs()

# 获取网卡属性
psutil.net_if_stats()

# 查看网卡流量
psutil.net_io_counters(pernic=True)

# 查看网卡历史流量
psutil.net_io_counters(pernic=True)

# 获取网络连接信息
psutil.net_connections()

# 获取进程的网络连接
p = psutil.Process(1014)
p.connections()

# 获取进程的
