import socket
import time


IP_ADDRS = "127.0.0.1"
PORT = 8000

class Server(object):
    def __init__(self, addr=IP_ADDRS, port=PORT):
        self.addr = addr
        self.port = port

    def create_server(self):
        # 创建一个tcp套接字
        tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 绑定地址
        tcp_server.bind((self.addr, self.port))
        tcp_server.listen(128)
        return tcp_server

    def run(self):
        # 创建tcp套接字
        tcp_server = self.create_server()
        while True:
            # 等待客户端的连接
            client_sock, client_addr = tcp_server.accept()
