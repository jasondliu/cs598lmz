import socket
import threading
import time
import sys

# 定义全局变量
HOST = '127.0.0.1'
PORT = 8000
ADDR = (HOST, PORT)

# 处理客户端请求
def handle(connfd):
    print("Connect from", connfd.getpeername())
    while True:
        data = connfd.recv(1024)
        if not data:
            break
        print(data.decode())
        connfd.send(b'OK')
    connfd.close()

# 创建套接字
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(ADDR)
s.listen(3)

# 接收客户端请求
