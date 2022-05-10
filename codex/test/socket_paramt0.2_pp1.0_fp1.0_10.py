import socket
socket.if_indextoname(3)

# 查看网卡的状态
import psutil
psutil.net_if_stats()

# 查看网卡的详细信息
import psutil
psutil.net_if_addrs()

# 获取网络连接信息
import psutil
psutil.net_connections()

# 获取当前网络连接信息
import psutil
psutil.net_connections(kind='inet')

# 获取本机IP
import socket
socket.gethostbyname(socket.gethostname())

# 获取本机IPV4
import socket
socket.gethostbyname_ex(socket.gethostname())[2][2]

# 获取本机IPV6
import socket
