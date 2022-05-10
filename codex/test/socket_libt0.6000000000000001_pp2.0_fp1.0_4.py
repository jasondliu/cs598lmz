import socket

class Server:
    def __init__(self, ip, port):
        self.__ip = ip
        self.__port = port
        self.__s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__s.bind((ip, port))
        self.__s.listen(5)
        self.__conn = None
        self.__addr = None

    def accept(self):
        self.__conn, self.__addr = self.__s.accept()

    def send(self, data):
        self.__conn.send(data)

    def recv(self, size=1024):
        return self.__conn.recv(size)

    def close(self):
        self.__s.close()

# server = Server('192.168.0.102', 9999)
# server.accept()
# print(server.recv())
# server.send(b'test')
# server.close()
