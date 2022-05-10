import threading
# Test threading daemon
import random
from random import randint
from threading import Thread
from time import sleep
from datetime import datetime

from http.server import HTTPServer, BaseHTTPRequestHandler
from io import BytesIO

from server import Server
from client import Client
from message import Message


## SERVER
# Setup server
server = Server('127.0.0.1', 6969)
# Start listening for clients
server.startListening()

# Broadcast message
# for client in server.clients:
#     server.broadcast(client, Message.makeMessage('{ "type": "ping" }'))

# Sleep main thread to not interrupt client thread
# time.sleep(1)


## CLIENT
# Connect to server
client = Client(Address('127.0.0.1', 6969))
client.connect()

# Sleep main thread to not interrupt client thread
# time.sleep(1)


## HANDLE MESSAGES
# Handle messages
while True:
    message = client.receiveMessage()

    if message is not None:
        data = message.getData
