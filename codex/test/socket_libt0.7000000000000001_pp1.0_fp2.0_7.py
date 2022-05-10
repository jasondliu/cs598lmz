import socket
import sys
import os
import threading
import time

class Server:
    def __init__(self, port):
        self.host = '127.0.0.1'
        self.port = port
        self.socket_list = []
        self.dir_path = './client_file_%d/' % port

    def run(self):
        if not os.path.exists(self.dir_path):
            os.mkdir(self.dir_path)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((self.host, self.port))
        s.listen(5)
        self.socket_list.append(s)
        while True:
            ready_to_read, ready_to_write, in_error = select.select(self.socket_list, [], [], 0)
            for sock in ready_to_read:
                if sock == s:
                    c, addr = s.accept()
