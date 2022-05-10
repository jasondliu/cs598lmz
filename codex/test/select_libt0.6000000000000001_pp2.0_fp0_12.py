import select
import socket
import sys
import threading
import time
import tkinter

from client_core import Core
from client_gui import GUI

class Client:


    SERVER_HOST = '0.0.0.0'
    SERVER_PORT = 8000
    RECEIVE_BUFFER = 4096
    TIMEOUT = 1

    def __init__(self):
        self.core = Core()
        self.gui = GUI(self.core, self.handle_gui_event)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.SERVER_HOST, self.SERVER_PORT))
        self.sock.settimeout(self.TIMEOUT)
