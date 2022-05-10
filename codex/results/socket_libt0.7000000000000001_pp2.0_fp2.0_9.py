import socket
import time

class Client():
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_addr = ('127.0.0.1', 65530)

    def sendCommand(self, command):
        self.sock.sendto(command, self.server_addr)
        time.sleep(0.2)

    def moveUp(self):
        self.sendCommand('w')

    def moveDown(self):
        self.sendCommand('s')

    def moveRight(self):
        self.sendCommand('d')

    def moveLeft(self):
        self.sendCommand('a')

    def stop(self):
        self.sendCommand('q')



client = Client()

def keyListener():
    while True:
        command = raw_input()
        if command == 'w':
            client.moveUp()
            continue
        if command == 's':
            client.moveDown()
            continue
        if command == 'a
