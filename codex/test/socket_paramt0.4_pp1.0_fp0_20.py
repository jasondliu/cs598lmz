import socket
socket.if_indextoname(2)

# 查看网卡的状态
import psutil
psutil.net_if_stats()

# 查看网卡的详细信息
psutil.net_if_addrs()

# 查看网络连接信息
psutil.net_connections()

# 查看网络流量状态
psutil.net_io_counters()

# 查看网络流量状态（按网卡）
psutil.net_io_counters(pernic=True)

# 查看系统的所有进程ID
psutil.pids()

# 查看指定进程ID的信息
