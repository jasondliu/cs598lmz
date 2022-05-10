import socket
import os
import sys
import platform
import time

class Server:
    def __init__(self):
        self.host = ''
        self.port = 9999
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.host, self.port))
        self.sock.listen(1)
        print("Listening...")

    def handleClient(self, client):
        while True:
            request = client.recv(1024)
            if not request:
                break
            client.send(request.upper())
        print("Closing connection")
        client.close()
        
    def run(self):
        while True:
            client, address = self.sock.accept() 
            print("Connection from: ", address)
            self.handleClient(client)


if __name__ == "__main__":
    Server().run()
