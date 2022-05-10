import socket
import threading
import time
import sys

class Client(threading.Thread):
    def __init__(self, _id, _name, _conn, _addr):
        threading.Thread.__init__(self)
        self.id = _id
        self.name = _name
        self.conn = _conn
        self.addr = _addr
        print '[+] New thread for client: ', self.id

    def run(self):
        print 'Client: ', self.id, ' Start!'
        while True:
            data = self.conn.recv(1024)
            if not data:
                break
            print '[' + self.name + '] ' + data
            for c in clients:
                c.conn.sendall('[' + self.name + '] ' + data)
        print 'Client: ', self.id, ' Exit!'
        self.conn.close()

HOST = ''
PORT = 8888
ADDR = (HOST, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK
