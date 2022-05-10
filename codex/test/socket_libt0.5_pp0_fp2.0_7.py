import socket
import threading
import time
import os
import random

def server_func(server_ip, server_port, client_port):
    # 创建socket对象
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 绑定端口
    server.bind((server_ip, server_port))
    # 开始监听
    server.listen()
    # 设置超时时间
    server.settimeout(5)
