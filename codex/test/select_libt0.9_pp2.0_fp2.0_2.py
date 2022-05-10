import select
import socket
import time


class MyServer(object):
    def __init__(self):
        self.s_handler = None

    def run(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        self.sock.bind(('127.0.0.1', 9999))

        self.sock.listen(5)

        self.sock.setblocking(0)

        # initialize a list
        self.epoll = select.epoll()

        # 注册要监听的socket
        self.epoll.register(self.sock.fileno(), select.EPOLLIN)

        # sockets from which we expect to read

        # sockets from which we expect to write

        # create a dictionary for sockets' file descriptors
        # key: file descriptor; value: socket object

        self.connections = {}
