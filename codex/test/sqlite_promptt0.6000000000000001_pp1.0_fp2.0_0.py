import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(":memory:").execute("select count(*) from sqlite_master").fetchone()
import time
import traceback
import os
import sys
import random
import struct
import subprocess
import json
import socket
import urllib

class Error(Exception):
    pass

class Logger(object):
    def __init__(self, file):
        self.file = file
        self.lock = threading.Lock()
    def log(self, message):
        self.lock.acquire()
        try:
            self.file.write(str(message) + "\n")
            self.file.flush()
        finally:
            self.lock.release()
    def close(self):
        self.file.close()

log = Logger(open("/var/log/mesh_node.log", "a"))

class Node(object):
    def __init__(self, name, port, database_file):
        self.name = name
        self.port = port
        self.database_file = database_file
        self.database = None
