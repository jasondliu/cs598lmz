import socket
socket.if_indextoname(3)

# 查看某个网络接口的索引号
import socket
socket.if_nametoindex('eth0')

# 获取本机网络接口的信息
import socket
print([(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1])

# 获取本机的MAC地址
import uuid
print(':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff) for ele in range(0,8*6,8)][::-1]))

# 获取本机的IP地址
import socket
print([(s.connect(('8.8.8.8', 53)), s
