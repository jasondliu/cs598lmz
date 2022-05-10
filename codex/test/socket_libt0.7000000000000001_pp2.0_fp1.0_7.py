import socket
import select
import threading
from _thread import *
import queue
import sys
import json
import random
import re
import math

#PYTHONPATH = "/usr/lib/python3"
#sys.path.append(PYTHONPATH)

from pymongo import MongoClient

def send_message(client_socket, message):
    if len(message) == 0:
        return
    try:
        client_socket.sendall(message.encode("utf-8"))
    except:
        print("send message error")

def receive_message(client_socket):
    try:
        client_socket.settimeout(10)
        message = client_socket.recv(2048).decode("utf-8")
        return message
    except:
        print("receive message error")
        return ""

class Server:
    def __init__(self):
        self.HOST = "127.0.0.1"
        self.PORT = 8888
        self.queue_list = []
