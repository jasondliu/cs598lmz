from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'I 2s f'
s.size = s.calcsize()
print(s.size)

# 如果需要创建大量的结构体实例，可以预先编译得到模板类
import socket
import struct
import binascii

# 创建一个原始套接字，然后绑定到公开网络接口
s = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0800))
s.bind(('eth0', socket.htons(0x0800)))

# 读取数据包
while True:
    pkt = s.recvfrom(2048)
    # 解析以
