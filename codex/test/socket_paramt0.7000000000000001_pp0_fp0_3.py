import socket
socket.if_indextoname(1)

# 查看当前机器所有网卡状态
for i in range(1,256):
    try:
        name = socket.if_indextoname(i)
        print(name)
    except:
        pass

# 获取所有网卡名称,get_if_name()
import netifaces
netifaces.interfaces()
netifaces.ifaddresses('en0')

# 获取所有网卡的ip地址,get_if_ip()
netifaces.ifaddresses('en0')[2][0]['addr']

# 获取所有网卡的mac地址,get_if_mac()
