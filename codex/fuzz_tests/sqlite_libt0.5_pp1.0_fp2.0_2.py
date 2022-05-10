import ctypes
import ctypes.util
import threading
import sqlite3
import time
import os
import sys
import re

# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------

# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------

def tprint(s):
    print '[%s] %s' % (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()), s)

# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------

class VpnService(object):
    def __init__(self):
        self.name = 'vpn'
        self.display_name = 'VPN Service'
        self.description = 'VPN Service'
        self.is_running = False
        self.is_stopping = False
        self.h_thread = None
        self.db_file = 'vpn.db'
        self.db_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), self.db_file)
        self.db_lock = threading.Lock()
        self.db_conn = None
       
