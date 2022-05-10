import socket
socket.if_indextoname(3)

# 打印所有的网卡
import netifaces
netifaces.interfaces()

# 打印某个网卡的所有ip地址
netifaces.ifaddresses('eth0')
# 获取某个网卡的ip地址
netifaces.ifaddresses('eth0')[netifaces.AF_INET][0]['addr']
# 打印所有网卡的ip地址
for i in netifaces.interfaces():
    print(i, netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr'])

# 打印本机所有ip地址
import netifaces
import socket

