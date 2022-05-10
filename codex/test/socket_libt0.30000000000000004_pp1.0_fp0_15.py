import socket
import sys
import time
import threading
import os
import re
import random

# 创建 socket 对象
serversocket = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)

# 获取本地主机名
host = socket.gethostname()

port = 9999

# 绑定端口号
serversocket.bind((host, port))

# 设置最大连接数，超过后排队
serversocket.listen(5)

print('服务器启动，等待客户端连接...')

while True:
    # 建立客户端连接
    clientsocket, addr = serversocket.accept()

