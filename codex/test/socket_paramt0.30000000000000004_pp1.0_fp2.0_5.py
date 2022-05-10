import socket
socket.if_indextoname(1)

# 查看网络接口状态
import psutil
psutil.net_if_stats()

# 获取网卡属性
import psutil
psutil.net_if_addrs()

# 获取网卡状态
import psutil
psutil.net_if_stats()

# 获取网卡流量统计
import psutil
psutil.net_io_counters()

# 获取网卡总流量统计
import psutil
psutil.net_io_counters(pernic=False)

# 获取网络连接信息
import psutil
psutil.net_connections()

# 获取网络连接信息
import psutil
