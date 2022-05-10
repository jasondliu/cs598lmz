import socket
socket.if_indextoname(3)

# 先安装netifaces
import netifaces as ni
ni.ifaddresses('eth0')
ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']  # 查看以太网的IP地址

# 查看物理地址
import uuid
uuid.UUID(int=uuid.getnode()).hex[-12:]

# 查看系统版本
import platform
platform.platform()
platform.architecture()
platform.version()
platform.uname()

# 系统信息
import os
os.name

# 查看CPU信息
import psutil
psutil.cpu_count()
psutil.cpu_count(logical=False)
psutil.cpu_times()

# 查看内存信息
psutil.virtual_memory()
ps
