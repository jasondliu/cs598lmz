import socket
socket.if_indextoname(1)

# 获取网络接口信息
import netifaces
netifaces.interfaces()

# 获取网络接口的IP地址
netifaces.ifaddresses('en0')

# 获取网络接口的MAC地址
netifaces.ifaddresses('en0')[netifaces.AF_LINK][0]['addr']

# 获取网络接口的IP地址
netifaces.ifaddresses('en0')[netifaces.AF_INET][0]['addr']

# 获取网络接口的子网掩码
netifaces.ifaddresses('en0')[netifaces.AF_INET][0]['netmask']

# 获取网络
