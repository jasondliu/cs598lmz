import socket
import sys
import time

from threading import Thread

from client import Client
from server import Server

class ClientThread(Thread):
    def __init__(self, client):
        Thread.__init__(self)
        self.client = client

    def run(self):
        self.client.run()

class ServerThread(Thread):
    def __init__(self, server):
        Thread.__init__(self)
        self.server = server

    def run(self):
        self.server.run()

def main():
    client = Client()
    server = Server()

    client_thread = ClientThread(client)
    server_thread = ServerThread(server)

    client_thread.start()
    server_thread.start()

    client_thread.join()
    server_thread.join()

if __name__ == "__main__":
    main()
