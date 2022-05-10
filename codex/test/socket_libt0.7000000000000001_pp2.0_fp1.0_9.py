import socket
import threading
import logging

class Server:
    def __init__(self, host, port, db):
        self.host = host
        self.port = port
        self.db = db

    def start(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((self.host, self.port))
        s.listen(10)
        while True:
            conn, addr = s.accept()
            logging.info('Connected with ' + addr[0] + ':' + str(addr[1]))
            threading.Thread(target = self.client_thread, args = (conn, addr)).start()

    def client_thread(self, conn, addr):
        while True:
            data = conn.recv(1024)
            if not data:
                break
            self.db.insert(data)
        conn.close()
