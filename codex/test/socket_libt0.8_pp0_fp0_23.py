import socket
import select
import os
import sys
import time
import json
from datetime import datetime
import threading

from conf import *
from server_utils import *

class Main(object):
    def __init__(self):
        self.statistics = Statistics()
        signal.signal(signal.SIGINT, self.clean_up)
        self.connections = {}

