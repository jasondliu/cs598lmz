import socket
import threading
import os
import time

def main():
    # 创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 绑定端口
    tcp_server_socket.bind(("", 7890))

    # 设置为监听状态
    tcp_server_socket.listen(128)

    while True:
        # 等待客户端的连接
        new_client_socket, client_addr = tcp_server_socket.accept()

        # 为客户端服务
        service_client(new_client_socket)

    # 关闭套接字
    tcp_server_socket.close()


def service_client(new_client_socket):
    """为客户端返回数据"""

    #
