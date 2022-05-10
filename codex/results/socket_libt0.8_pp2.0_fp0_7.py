import socket
import sys
import time


class Client(object):
    def __init__(self, ip='127.0.0.1', port='5555'):
        self.s = self.__create_socket(ip, port)

    def __create_socket(self, ip, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, int(port)))
        return s

    def send(self, string='Hello World!'):
        self.s.send(string)
        data = self.s.recv(1024)
        self.s.close()
        return data

    def close_connection(self):
        self.s.close()


if __name__ == '__main__':
    if len(sys.argv) == 3:
        c = Client(sys.argv[1], sys.argv[2])
    else:
        c = Client()

    while True:
        s = raw_input('please input data: ')
        if s == 'end':
