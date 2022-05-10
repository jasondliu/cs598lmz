import socket
import sys
import time
import re
import os
import ctypes
import threading
import Queue
import subprocess
import signal
import base64
import traceback
import platform
import psutil

from datetime import datetime
from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Hash import SHA256

from lib import config
from lib import helper
from lib import database
from lib import connections
from lib import messages
from lib import encryption

class Listener:
    def __init__(self, address, port, max_connections):
        self.address = address
        self.port = port
        self.max_connections = max_connections
        self.active_connections = 0
        self.running = False
        self.socket = None
        self.threads = []

    def _start_server(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

