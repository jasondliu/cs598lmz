import select
import sys
import time

class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.settimeout(2)
        self.socket.connect((self.host, self.port))
        self.socket.setblocking(False)
    
    def __del__(self):
        self.socket.close()

    def send(self, message):
        self.socket.send(bytes(message, 'utf-8'))
        return self.socket.recv(1024).decode('utf-8')

    def receive(self):
        return self.socket.recv(1024).decode('utf-8')

def main():
    if len(sys.argv) < 3:
        print('Usage: {} <host> <port>'.format(sys.argv[0]))
        return

    host = sys.argv[1]
