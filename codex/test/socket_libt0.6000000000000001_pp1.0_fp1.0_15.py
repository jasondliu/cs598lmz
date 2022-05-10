import socket
import time
import datetime
import sys
import os
import re
import struct
import math
import copy
import json

class Logger:
    def __init__(self, path):
        self.terminal = sys.stdout
        self.log = open(path, "a")
        self.log.write(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '\n')

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)
    
    def close(self):
        self.log.close()

class Server:
    def __init__(self, path=None):
        if path is None:
            path = os.path.join(os.getcwd(), 'logs')
        if not os.path.exists(path):
            os.mkdir(path)
