import ctypes
import ctypes.util
import threading
import sqlite3
import time
import hashlib
import requests
import json
import sys
import os

START_SERVER_SCRIPT = "start_server.py"
GRANTED_KEY = "granted_key"

# globals
global client_list
global connection_list
global key_list
global key_lock
global db_name
global terminal_mode

db_name = "database.db"
terminal_mode = True

class ClientThread(threading.Thread):
    def __init__(self, ip, port, clientsocket, key):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.clientsocket = clientsocket
        self.key = key

    def run(self):
        print("\n[+] Accepting connections from: %s:%s" % (self.ip, self.ip))
        print("[+] Sent key %s to %s:%s" % (self.key, self.ip, self.port))
        self.clientsocket.send(
