import socket
socket.if_indextoname(3)

# 使用if_indextoname() 函数将索引号转换为网络接口名称
# socket.if_indextoname(3)

# 使用if_nameindex() 函数获取网络接口的索引号和名称
import socket
socket.if_nameindex()

# 使用if_nameindex() 函数获取网络接口的索引号和名称
# socket.if_nameindex()

# 使用ioctl() 函数获取网络接口的索引号
import socket
socket.ioctl(socket.socket(socket.AF_INET, socket.SOCK_DGRAM), 0x89
