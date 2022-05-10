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
    while True:
        try:
            # 接受客户端的连接
            client, addr = server.accept()
            # 设置超时时间
            client.settimeout(5)
            # 接收客户端的消息
            msg = client.recv(1024)
            # 打印消息
           
