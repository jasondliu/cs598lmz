import select
import sys
import time

class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((host,port))
        self.socket.setblocking(0)
        self.inputs = [self.socket]

    def run(self):
        while True:
            readable, writable, exceptional = select.select(self.inputs, [], self.inputs)
            for s in readable:
                if s is self.socket:
                    data = s.recv(1024)
                    if data:
                        print(data)
                    else:
                        print('disconnected')
                        self.inputs.remove(s)
                        s.close()
            for s in exceptional:
                print('exception')
                self.inputs.remove(s)
                s.close()

