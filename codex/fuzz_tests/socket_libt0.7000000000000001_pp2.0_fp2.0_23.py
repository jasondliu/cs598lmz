import socket
import threading
import json
import sys
import os
import time
import subprocess

# A dictionary of online users
online_user = {}
# A dictionary of user info
user_info = {}


class Client():
    def __init__(self, host='127.0.0.1', port=9999):
        self.host = host
        self.port = port
        self.sock = socket.socket()
        self.event = threading.Event()

    def start(self):
        try:
            self.sock.connect((self.host, self.port))
        except Exception as e:
            print(e)
            sys.exit()
        print('''\033[33;1m
            *****************************
            ** Welcome to the chatroom **
            *****************************
            \033[0m''')
        # Create threading
        thread_send = threading.Thread(target=self.send_msg)
        thread_send.daemon = True
        thread_send.start()

        thread_recv = threading.Thread
