import socket
import threading
import sys

class Server:
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connections = []
    def __init__(self):
        self.soc.bind(('0.0.0.0',10000))
        self.soc.listen(1)
    def handler(self, c, a):
        while True:
            data = c.recv(1024)
            for connection in self.connections:
                connection.send(bytes(data))
            if not data:
                print(str(a[0])+':'+str(a[1]),"disconnected")
                self.connections.remove(c)
                c.close()
                break
    def run(self):
        while True:
            c,a = self.soc.accept()
            cThread = threading.Thread(target = self.handler, args = (c,a))
            cThread.daemon = True
            cThread.start()
            self.connections.append(c)
            print(str
