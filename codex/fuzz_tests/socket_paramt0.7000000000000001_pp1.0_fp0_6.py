import socket
socket.if_indextoname(2)

# 字节序转换
import socket
socket.ntohl(0x12345678)

# 转换为网络字节序列
import socket
socket.htonl(0x12345678)

# 转换为主机字节序列
import socket
socket.htons(0x1234)

# 转换为网络字节序列
import socket
socket.ntohs(0x1234)

# 如果你想获取当前主机的某个IP地址
# 可以使用socket.gethostbyname()方法来获取，结果是一个IP地址的字符串
# 如果
