import socket
import sys
import time
import threading

class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))
        self.sock.settimeout(2)
        self.threads = []

    def send(self, msg):
        try:
            self.sock.sendall(msg)
        except socket.error:
            print 'Send failed'
            sys.exit()

    def receive(self):
        try:
            data = self.sock.recv(1024)
        except socket.timeout:
            #print 'No data received'
            return None
        except socket.error:
            print 'Receive failed'
            sys.exit()
        return data

    def close(self):
        self.sock.close()

    def start(self):
        self.threads.append(threading.Thread(target=
