import socket
import threading
from datetime import datetime
from time import sleep

from multiprocessing import Process

import sys

from subprocess import check_output, CalledProcessError

from os import path

HOST = '127.0.0.1'    # The remote host
PORT = 50007              # The same port as used by the server
BUFFSIZE = 1024

# This class holds the data of one node that is available in the system
class Node:
    def __init__(self, name, ip, port):
        self.name = name
        self.ip = ip
        self.port = port
        self.status = 'up'
        self.last_keep_alive = datetime.now()

    def update_last_keep_alive(self):
        self.last_keep_alive = datetime.now()

    def set_status(self, status):
        self.status = status

# This class holds the state of the system
class State:
    def __init__(self):
        self.nodes = []
        self.n
