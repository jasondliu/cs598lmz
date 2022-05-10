import ctypes
import ctypes.util
import threading
import sqlite3
import os
import subprocess
import sys
import time
from datetime import datetime
import re
import traceback
import signal
import socket
import json

from lib.utils import *
from lib.messages import *
from lib.exceptions import *
from lib.config import *

from lib.logger import Logger

class NetworkManager(threading.Thread):
    def __init__(self, queue, config, logger):
        threading.Thread.__init__(self, name='NetworkManager')
        self.queue = queue
        self.config = config
        self.logger = logger
        self.stop = False
        self.server = None
        self.threads = []
        self.sockets = []
        self.socket_lock = threading.Lock()
        self.client_data = {}

