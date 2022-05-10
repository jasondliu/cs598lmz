import socket
socket.if_indextoname(3)

#%%
# TCP 客户端
import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 建立连接
s.connect(('www.sina.com.cn',80))

#%%
import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

for data in [b'Michael',b'Tracy',b'Sarah']:
    # 发送数据
    s.sendto(data,('127.0.0.1',9999))
    # 接收数据
    print(s.recv(1024).decode('utf-8'))

s.close()

#%%
# UDP 客户端
import socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

