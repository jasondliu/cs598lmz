import socket
import threading
import os, signal
import sys
import re

class TCP_Server:
    def __init__(self, IP, port):
        self.server_socket = socket.socket(socket.AF_INET,
                                           socket.SOCK_STREAM)
        self.server_socket.bind((IP, port))
        self.server_socket.listen(5)
        self.open_client_sockets = []
        self.messages_to_send = []

    def listen(self):
        try:
            self.server_socket.listen(5)
        except:
            print("Error with listening to the server\n")

    def accept(self):
        try:
            client_socket, address = self.server_socket.accept()
            print("New connection to: " + str(address) + "\n")
            self.open_client_sockets.append(client_socket)
            self.listen_to_client(client_socket, address)
        except:
            print("Error with accepting the client\n")

   
