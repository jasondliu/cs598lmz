import socket
socket.if_indextoname(2)
socket.if_nametoindex('en0')

# 将 ip 地址转换成二进制的整数
socket.htons(0xc0a8) # 3232235520
socket.htonl(0xa8c0) # 1715192480

# 其他工具函数
socket.inet_pton(socket.AF_INET, '192.168.1.1') # b'\xc0\xa8\x01\x01'
socket.inet_ntop(socket.AF_INET, b'\xc0\xa8\x01\x01') #'192.168.1.1'

# 获取输入输出队列的大小
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF) # 9216

