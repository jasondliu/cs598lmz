import socket
socket.if_indextoname(3)

# 查看网卡信息
import psutil
psutil.net_if_addrs()

# 查看网络连接信息
psutil.net_connections()

# 获取进程pid
import os
os.getpid()

# 获取父进程pid
os.getppid()

# 获取父进程
import psutil
p = psutil.Process(os.getpid())
p.parent()

# 获取父进程的父进程
p.parent().parent()

# 获取所有父进程
p.parents()

# 获取进程名称
p.name()

# 获取进程exe路径
p.
