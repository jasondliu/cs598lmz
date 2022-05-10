import socket
import threading
import time
import sys
import os
import re
import random
import string

from . import config
from . import util
from . import log
from . import const
from . import exception
from . import protocol
from . import plugin

class Client(object):
    def __init__(self, host, port, username, password, plugin_dir, log_dir):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.plugin_dir = plugin_dir
        self.log_dir = log_dir
        self.sock = None
        self.protocol = None
        self.plugin = None
        self.logger = None
        self.is_connected = False
        self.is_logged_in = False
        self.is_logged_out = False
        self.is_stopped = False
        self.is_stopping = False
        self.is_running = False
        self.is_paused = False
        self.is_pausing = False
       
