import socket
import threading
import time
import os

# 创建一个socket对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 获取本地主机名
host = socket.gethostname()
# 设置端口
port = 9999
# 绑定端口
s.bind((host, port))
# 设置最大连接数，超过后排队
s.listen(5)
print('Server start at: %s:%s' % (host, port))
print('wait for connection...')


def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
