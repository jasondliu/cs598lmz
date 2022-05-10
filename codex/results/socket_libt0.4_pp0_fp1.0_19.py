import socket
import sys
import time
import threading
import Queue
import os
import re
import json
import logging
import logging.handlers

# global variables
HOST = ''
PORT = 8888

# create socket (SOCK_STREAM means a TCP socket)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# bind the socket to a public host, and a well-known port
sock.bind((HOST, PORT))

# become a server socket
sock.listen(1)

# queue for the messages
message_queue = Queue.Queue()

# dictionary for the clients
clients = {}

# dictionary for the clients
rooms = {}

# dictionary for the clients
room_names = {}

# dictionary for the clients
room_counts = {}

# logging
LOG_FILENAME = 'log.out'
logger = logging.getLogger()
logger
