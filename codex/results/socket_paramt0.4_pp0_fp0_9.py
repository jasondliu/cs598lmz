import socket
socket.if_indextoname(3)

# 查看网卡状态
import netifaces
netifaces.interfaces()
netifaces.ifaddresses('lo')
netifaces.ifaddresses('eth0')
netifaces.ifaddresses('wlan0')

# 查看网卡状态
import psutil
psutil.net_if_addrs()
psutil.net_if_stats()

# 查看网络连接
import psutil
psutil.net_connections()

# 查看进程
import psutil
psutil.pids()
p = psutil.Process(5)
p.name()
p.exe()
p.cwd()
p.status()
p.create_time()
p.uids()
p.gids()
p.cpu_times()
p.memory_info()
p.open_files()
p.connections()
p.num_threads()
p
