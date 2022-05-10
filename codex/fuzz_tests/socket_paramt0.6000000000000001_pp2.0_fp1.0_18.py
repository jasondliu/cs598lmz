import socket
socket.if_indextoname(2)

# 获取本机IP地址
import socket
socket.gethostbyname(socket.gethostname())

# 获取本机MAC地址
import uuid
uuid.UUID(int = uuid.getnode()).hex[-12:]

# 获取本机CPU信息
import cpuinfo
cpuinfo.get_cpu_info()['brand']

# 获取本机磁盘信息
import psutil
print(psutil.disk_partitions())
print(psutil.disk_usage('/'))
print(psutil.disk_io_counters())

# 获取本机用户信息
import pwd
pwd.getpwuid(0)

# 获取本机网络信息
import psutil
print(psutil.net_if_addrs())

