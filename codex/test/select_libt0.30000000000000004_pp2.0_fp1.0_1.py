import select
import socket
import sys
import time
import threading
import Queue

from datetime import datetime

class Server(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))
        self.sock.listen(5)
        self.inputs = [self.sock]
        self.outputs = []
        self.message_queues = {}
        self.clients = {}
        self.threads = []
        self.thread_id = 0
        self.thread_lock = threading.Lock()
        self.thread_id_lock = threading.Lock()
        self.thread_id_lock.acquire()
        self.thread_id_lock.release()
