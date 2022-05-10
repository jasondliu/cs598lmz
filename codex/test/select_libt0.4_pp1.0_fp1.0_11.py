import select
import socket
import sys
import time
import random
import os
import errno
from threading import Thread
import threading
import json
from time import sleep
import logging
import logging.handlers

from uuid import getnode as get_mac

import requests
import urllib

from collections import defaultdict

from config import *

class Server(object):
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.id = self.ip + ':' + str(self.port)
        self.is_alive = True
        self.last_seen = time.time()
        self.files = []

class File(object):
    def __init__(self, name, size, id):
        self.name = name
        self.size = size
        self.id = id
        self.servers = []

class Client(object):
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
