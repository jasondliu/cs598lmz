import socket
import time
import threading
import os
import sys

# 设置全局变量
HOST = ''
PORT = 8001
BUFSIZ = 1024
ADDR = (HOST, PORT)

# 创建套接字
tcpSerSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpSerSock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# 绑定地址
tcpSerSock.bind(ADDR)

# 监听
tcpSerSock.listen(5)

# 设置为非阻塞
tcpSerSock.setblocking(False)

# 设置为非输出缓冲
tcpSerSock.setsockopt(socket.IPPROTO_TCP, socket.TC
