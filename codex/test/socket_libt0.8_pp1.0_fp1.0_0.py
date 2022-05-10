import socket
import threading
import time


class Host:
    def __init__(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(('127.0.0.1', 8090))
        self.server_socket.listen(5)

    def send_msg(self, conn, data):
        pass

    def get_msg(self, conn, data):
        pass

    def handle(self, conn, addr):
        print('123')
        while True:
            data = conn.recv(1024)
            print(data)
            self.get_msg(conn, data)
            if data:
                conn.sendall(data.upper())
            else:
                conn.close()
                break

    def run(self):
        while True:
            conn, addr = self.server_socket.accept()
            thread = threading.Thread(target=self.handle, args=[conn, addr])
            thread.start()


