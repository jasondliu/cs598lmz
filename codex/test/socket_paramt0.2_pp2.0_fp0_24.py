import socket
socket.if_indextoname(3)

# 列出所有网络接口
import netifaces
netifaces.interfaces()

# 获取某个网络接口的信息
netifaces.ifaddresses('lo')

# 获取某个网络接口的IP地址
netifaces.ifaddresses('lo')[netifaces.AF_INET][0]['addr']

# 获取本机所有网卡的IP地址
for i in netifaces.interfaces():
    print(i, netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr'])

# 获取本机所有网卡的MAC地址
