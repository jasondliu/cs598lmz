import socket

class Server:
    def __init__(self, ip, port, conn=None):
        self.ip = ip
        self.port = port
        self.conn = conn

    def create_socket(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((self.ip, self.port))
        self.s.listen(1)

    def connect(self):
        self.conn, self.addr = self.s.accept()

    def disconnect(self):
        self.conn.close()
        self.s.close()

    def receive(self):
        return self.conn.recv(1024).decode()

    def send(self, msg):
        self.conn.send(msg.encode())
