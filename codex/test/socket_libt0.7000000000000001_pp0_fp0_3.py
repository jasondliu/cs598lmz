import socket
import sys

modules = {}

def register(module):
    modules[module.__name__] = module

class Message(object):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

class Channel(object):
    def __init__(self, name):
        self.name = name
        self.clients = []
        self.messages = []

    def broadcast(self, msg):
        self.messages.append(msg)
        for client in self.clients:
            client.send(str(msg))

    def send(self, client, msg):
        client.send(str(msg))

    def join(self, client):
        self.clients.append(client)

    def part(self, client):
        self.clients.remove(client)

    def has_client(self, client):
        return client in self.clients

    def __str__(self):
        return self.name

