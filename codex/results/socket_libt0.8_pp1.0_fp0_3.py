import socket
import threading
import urllib.request



class Server:
    def __init__(self, host, port):
        self.HOST = host
        self.PORT = port
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((self.HOST, self.PORT))
        self.s.settimeout(5)

    def listen(self):
        self.s.listen(5)
        while True:
            try:
                conn, addr = self.s.accept()
                threading.Thread(target=self.client, args=(conn, addr)).start()
            except socket.timeout as e:
                print(str(e))
            except urllib.error.HTTPError as e:
                print(str(e))
                continue

    def client(self, conn, addr):
        try:
            data = conn.recv(1024)
        except ConnectionResetError as e:
            print(str(e))
        if data:
            if data == b
