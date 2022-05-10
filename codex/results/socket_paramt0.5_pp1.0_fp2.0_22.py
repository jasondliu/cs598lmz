import socket
socket.if_indextoname(3)

# 网络字节序和主机字节序
socket.ntohs(0x1234)
socket.ntohl(0x12345678)
socket.htons(0x1234)
socket.htonl(0x12345678)

# 地址转换函数
socket.inet_aton('127.0.0.1')
socket.inet_ntoa(b'\x7f\x00\x00\x01')
socket.inet_pton(socket.AF_INET, '127.0.0.1')
socket.inet_ntop(socket.AF_INET, b'\x7f\x00\x00\x01')
socket.inet_pton(socket.AF_INET6, '::1')
socket.inet_ntop(socket.AF_INET6, b'\x00' * 15 + b'\x01')

# 主机名和
