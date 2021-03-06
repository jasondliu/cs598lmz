import socket
import threading
import time
import sys
import os

# 创建socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定端口
s.bind(('127.0.0.1', 9999))

# 监听端口
s.listen(5)
print('Waiting for connection...')

# 接受一个新连接
def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s
