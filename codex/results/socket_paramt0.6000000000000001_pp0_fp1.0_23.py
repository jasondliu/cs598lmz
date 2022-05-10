import socket
socket.if_indextoname(4)

# 将接口名称转换为索引
socket.if_nametoindex('eth0')

# 网络地址转换函数
socket.inet_aton('127.0.0.1')

# 网络地址转换函数
socket.inet_ntoa(b'\x7f\x00\x00\x01')

# 返回套接字描述符的类型
socket.SOCK_STREAM

# 返回套接字的地址族
socket.AF_INET

# 返回套接字的类型
socket.SOCK_DGRAM

# 返回套接字的类型
socket.S
