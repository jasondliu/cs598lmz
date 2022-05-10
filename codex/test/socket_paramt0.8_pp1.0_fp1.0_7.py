import socket
socket.if_indextoname(dev)
'''

# 获取指定网卡的ip和子网掩码
'''
ip = socket.if_indextoname(dev)# 获取网卡对应的ip
print(ip)
import fcntl
import struct

str_ip = socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s', bytes(dev[:15], encoding='utf-8')))[20:24])
str_netmask = socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s', bytes(dev[:15], encoding='utf-8')))[20:24])
print(str_ip)
print(str_netmask)
'''

# 获取指定网卡的ip和子网掩码
'''
import f
