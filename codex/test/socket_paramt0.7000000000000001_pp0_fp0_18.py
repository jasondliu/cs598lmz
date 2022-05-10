import socket
socket.if_indextoname('1')

# 查看当前网络接口
import psutil
psutil.net_if_addrs()

# 查看系统分区表
import psutil
psutil.disk_partitions()

# 查看网络连接
import psutil
psutil.net_connections()
