import socket
socket.if_indextoname(3)

# 查看网卡的状态
import psutil
psutil.net_if_stats()

# 查看网卡的详细信息
import psutil
psutil.net_if_addrs()

# 查看网卡的流量信息
import psutil
psutil.net_io_counters(pernic=True)

# 查看网络连接信息
import psutil
psutil.net_connections()

# 查看网络连接信息
import psutil
psutil.net_connections(kind='inet')

# 查看网络连接信息
import psutil
psutil.net_connections(kind='inet4')

# 查看网络连
