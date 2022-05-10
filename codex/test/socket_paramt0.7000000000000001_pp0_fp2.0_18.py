import socket
socket.if_indextoname(12)

# 将一个IP地址转化为一个整数(用网络字节顺序)
socket.htonl(3232235777)

# 将一个字符串转换为一个整数(用网络字节顺序)
socket.ntohl(3232235777)

# 将一个IP地址转化为一个整数(用网络字节顺序)
socket.htons(20000)

# 将一个字符串转换为一个整数(用网络字节顺序)
socket.ntohs(20000)
