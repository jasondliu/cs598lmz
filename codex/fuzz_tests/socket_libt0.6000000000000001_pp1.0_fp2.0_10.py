import socket
from threading import Thread
from time import sleep

from server.client_thread import ClientThread
from server.server_config import ServerConfig
from server.server_message import ServerMessage


class Server:
    def __init__(self):
        self.host = ServerConfig.HOST
        self.port = ServerConfig.PORT
        self.clients = []
        self.chat_history = []
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.host, self.port))
        self.sock.listen()

    def accept_clients(self):
        while True:
            client_sock, client_address = self.sock.accept()
            print(f"{client_address} has connected.")
            client = ClientThread(client_sock, client_address, self)
            client.start()
            self.clients.append(client)

    def broadcast(self, msg):
        for client in self.clients:
            try:
                client
