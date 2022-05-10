import select
import socket
import time
import threading
import sys


# 创建socket对象，并设置端口号
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_addr = ("127.0.0.1", 8080)

# 告诉系统，我们要使用这个端口来接受连接
server.bind(server_addr)

# 开始监听连接
server.listen(10)

# 添加地址的容器
inputs = [server, ]

# 表示当前服务器中的连接
outputs = []

#
