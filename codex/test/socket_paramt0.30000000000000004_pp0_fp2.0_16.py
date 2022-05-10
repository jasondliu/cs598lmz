import socket
socket.if_indextoname(1)

# 获取本机网卡的网关
import netifaces
netifaces.gateways()

# 获取本机网卡的ip地址
import netifaces
netifaces.ifaddresses('eth0')

# 获取本机网卡的mac地址
import netifaces
netifaces.ifaddresses('eth0')[netifaces.AF_LINK][0]['addr']

# 获取本机网卡的子网掩码
import netifaces
netifaces.ifaddresses('eth0')[netifaces.AF_INET][0]['netmask']

# 获取本机网卡的网关
import netifaces
netifaces.gateways()['default'][netifaces.AF_INET][0]

# 获取
