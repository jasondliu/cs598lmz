import socket
import sys
import struct
import os
import time
from datetime import datetime
import threading
from threading import Thread, Lock
from random import randint
from collections import defaultdict
import server_utils as utils

global_seq_num = 0
global_timer = None
global_timer_lock = Lock()

def get_seq_num():
    """Get the sequence number of this message"""
    global global_seq_num
    global_seq_num += 1
    return global_seq_num

def get_time():
    """Get the time that has passed since the timer started"""
    global global_timer
    return time.time() - global_timer

class Server:
    """Server class for handling all communication with clients"""

    def __init__(self, host, port, config_file):
        """Initialise server with host, port and config file"""
        self.host = host
        self.port = port
        self.config_file = config_file
        self.conn_dict = {}  # client connection socket: client object
        self.message_dict
