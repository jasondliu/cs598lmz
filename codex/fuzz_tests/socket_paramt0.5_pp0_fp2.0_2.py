import socket
socket.if_indextoname(3)

# 打印系统信息
import os
print(os.name)
# 打印系统详细信息
import platform
print(platform.uname())

# 打印系统所有网络接口信息
import netifaces
print(netifaces.interfaces())

# 打印某个网络接口的详细信息
print(netifaces.ifaddresses('en0'))

# 打印lo0的第一个IP地址
print(netifaces.ifaddresses('lo0')[2][0]['addr'])
