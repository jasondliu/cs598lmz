import socket
socket.if_indextoname(3)

# 查看接口信息
import netifaces
netifaces.interfaces()

# 查看接口ip地址
# netifaces.ifaddresses('enp4s0')
netifaces.ifaddresses('lo')

# 查看接口的具体的ip地址
netifaces.ifaddresses('lo')[netifaces.AF_INET]

# 查看接口的具体的ipv4地址
netifaces.ifaddresses('lo')[netifaces.AF_INET][0]['addr']

# 查看本机的ip地址
