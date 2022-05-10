import socket
socket.if_indextoname(3)

# 查看网卡信息
import netifaces
netifaces.interfaces()

# 查看网卡的IP地址
netifaces.ifaddresses('eth0')

# 查看网卡的MAC地址
netifaces.ifaddresses('eth0')[netifaces.AF_LINK][0]['addr']

# 查看网卡的IPv4地址
netifaces.ifaddresses('eth0')[netifaces.AF_INET][0]['addr']

# 查看网卡的IPv6地址
netifaces.ifaddresses('eth0')[netifaces.AF_INET6][0]['addr']

# 查看网卡的IPv4地址和子网掩码
