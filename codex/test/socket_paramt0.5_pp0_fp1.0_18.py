import socket
socket.if_indextoname(3)

# 打印网络接口数量
import netifaces
netifaces.interfaces()

# 打印接口状态
netifaces.ifaddresses('en0')

# 获取接口IP地址
netifaces.ifaddresses('en0')[netifaces.AF_INET][0]['addr']

# 获取接口MAC地址
netifaces.ifaddresses('en0')[netifaces.AF_LINK][0]['addr']
