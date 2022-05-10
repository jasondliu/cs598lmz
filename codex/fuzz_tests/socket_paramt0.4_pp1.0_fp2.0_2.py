import socket
socket.if_indextoname(3)

# 查看网卡状态
import netifaces
netifaces.ifaddresses('eth0')

# 查看网络连接
import psutil
psutil.net_connections()

# 获取本机ip
import socket
def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()

    return ip

# 获取本机mac
import uuid
def get_mac_address():
    mac=uuid.UUID(int = uuid.getnode()).hex[-12:]
    return ":".join([mac[e:e+2] for e in range(0,11,2)])

# 获取本机cpu
